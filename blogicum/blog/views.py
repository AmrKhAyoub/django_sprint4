from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category, User, Comment

# --------------------------------------

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.views.generic import ListView

from django.views.generic import UpdateView

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PostForm , CommentForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse


POSTS_PER_PAGE = 10


def index(request):
    template = 'blog/index.html'
    now = timezone.now()
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        pub_date__lte=now,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')

    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.filter(
        pub_date__lte=timezone.now(),
        is_published=True
    ).order_by('-pub_date')

    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        pk=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    comments = post.comments.select_related('author')
    form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render(request, template, context)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:index')
    template_name = 'registration/registration_form.html'


class ProfileListView(ListView):
    model = Post
    template_name = 'blog/profile.html'
    paginate_by = 10
    # نحدد اسم الكائن في السياق ليكون page_obj ليتوافق مع قوالب المشروع والتقسيم
    context_object_name = 'page_obj'

    def get_queryset(self):
        # 1. جلب المستخدم صاحب الملف الشخصي أو إرجاع 404 إذا لم يوجد
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        
        # 2. إنشاء الاستعلام الأساسي مع تحسين الأداء (select_related) لجلب بيانات القسم والمكان
        # هذا ضروري لعرض الصور والبيانات المرتبطة بكفاءة
        queryset = Post.objects.filter(author=self.author).select_related('category', 'location')
        
        # 3. منطق المهمة الخامسة:
        # إذا كان المستخدم المسجل (request.user) ليس هو صاحب الملف الشخصي (self.author)
        # نقوم بفلترة المنشورات لعرض المنشورة فقط والمنتمية لأقسام منشورة وتاريخها ليس في المستقبل
        if self.request.user != self.author:
            queryset = queryset.filter(
                pub_date__lte=timezone.now(),
                is_published=True,
                category__is_published=True
            )
       
        # ترتيب المنشورات من الأحدث للأقدم
        return queryset.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        # إضافة بيانات صاحب الملف الشخصي للسياق لعرض اسمه في القالب
        context = super().get_context_data(**kwargs)
        context['profile'] = self.author
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    template_name = 'blog/user.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy(
            'blog:profile',
            kwargs={
                'username': self.request.user.username
            }
        )


@login_required
def post_create(request):
    template = 'blog/create.html'
    form = PostForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('blog:profile', username=request.user.username)

    context = {'form': form}
    return render(request, template, context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'  # استخدام نفس قالب الإنشاء حسب التعليمات

    def test_func(self):
        # التحقق من أن المستخدم الحالي هو مؤلف المنشور
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        # إذا لم يكن المستخدم هو المؤلف، يتم تحويله لصفحة عرض المنشور
        from django.shortcuts import redirect
        return redirect('blog:post_detail', id=self.kwargs['post_id'])

    def get_success_url(self):
        # بعد التعديل الناجح، التوجيه لصفحة المنشور
        return reverse('blog:post_detail', kwargs={'id': self.object.pk})


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('blog:post_detail', id=post_id)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'id': self.object.post.id})
