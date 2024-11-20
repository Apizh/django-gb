from django.http import HttpRequest #, HttpResponse
from django.shortcuts import render
from timeit import default_timer

# def shop_index(request: HttpRequest):
#     print(request.method)
#     print(request.path)
#     print(request.headers)
#     return HttpResponse("<h1>Hello world, было создано благодаря добавлению приложения в settings, в корневом проекте, добавлением include обработке маршрутов в urls.py, созданию</h1>")

def shop_index(request: HttpRequest):
    data = [
        ('Apple', 1.2),
        ('Banana', 0.8),
        ('Orange', 1.5),
        ('Grape', 0.9),
        ('Pear', 1.1),
        ('Cherry', 1.3),
        ('Melon', 1.4),
        ('Pineapple', 1.7),
        ('Mango', 1.6),
        ('Strawberry', 1.8),
        ('Blueberry', 1.9),
        ('Peach', 2.0),
    ]
    context = {
        'data' : data,
        'time_running': default_timer(),
    }
    return render(request, 'shop/shop-index.html', context=context)
