from django.http import HttpRequest #, HttpResponse
from django.shortcuts import render


# def shop_index(request: HttpRequest):
#     print(request.method)
#     print(request.path)
#     print(request.headers)
#     return HttpResponse("<h1>Hello world, было создано благодаря добавлению приложения в settings, в корневом проекте, добавлением include обработке маршрутов в urls.py, созданию</h1>")

def shop_index(request: HttpRequest):
    return render(request, 'shop/shop-index.html')
