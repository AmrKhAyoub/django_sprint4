from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


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
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
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
    context = {
        'category': category,
        'post_list': post_list,
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
    context = {'post': post}
    return render(request, template, context)
