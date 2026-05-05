from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AboutView(TemplateView):
    # تحديد القالب الخاص بصفحة "حول المشروع"
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    # تحديد القالب الخاص بصفحة "القواعد والشروط"
    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    # كود عرض صفحة الخطأ 404
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    # كود عرض صفحة الخطأ 403 (فشل التحقق من CSRF)
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    # كود عرض صفحة الخطأ 500
    return render(request, 'pages/500.html', status=500)
