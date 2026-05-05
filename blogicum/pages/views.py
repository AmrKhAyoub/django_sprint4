from django.shortcuts import render

# Create your views here.


def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)


def page_not_found(request, exception):
    # كود عرض صفحة الخطأ 404
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    # كود عرض صفحة الخطأ 403 (فشل التحقق من CSRF)
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    # كود عرض صفحة الخطأ 500
    return render(request, 'pages/500.html', status=500)
