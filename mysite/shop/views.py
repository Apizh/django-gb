from django.http import HttpRequest #, HttpResponse
from django.shortcuts import render
from timeit import default_timer

# def shop_index(request: HttpRequest):
#     print(request.method)
#     print(request.path)
#     print(request.headers)
#     return HttpResponse("<h1>Hello world, было создано благодаря добавлению приложения в settings, в корневом проекте, добавлением include обработке маршрутов в urls.py, созданию</h1>")

def shop_index(request: HttpRequest):
    context = {
        'time_running': default_timer(),
    }
    return render(request, 'shop/shop-index.html', context=context)
