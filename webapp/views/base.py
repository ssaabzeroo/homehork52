from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.views.cat import Cat


def index_view(request: WSGIRequest):
    print(f'GET first {request.POST}')
    name = request.GET.get('name')
    cat = Cat(name)

    if request.method == 'POST':
        return render(request, 'article_create.html', context=name)

    else:
        return render(request, 'index.html')
