from django.shortcuts import render


def page_forbidden(request, *args, **kwargs):
    return render(request, 'errors/403.html', status=403)


def page_not_found_local(request, *args, **kwargs):
    return render(request, 'errors/404.html', status=404)


def server_error(request, *args, **kwargs):
    return render(request, 'errors/500.html', status=500)
