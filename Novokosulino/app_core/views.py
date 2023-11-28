from django.shortcuts import render
from django.conf import settings
from app_news.models import Post


menu = ['на Главную страницу', 'Графики', 'Таблицы']


def index(request):
    posts = Post.objects.filter(status='ACT').order_by("order")
    context = {
        'posts': posts,
        'title': 'Главная страница',
    }
    return render(request, "app_core/index.html", context)


def management(request):
    return render(request, "app_core/management.html", {'menu': menu, 'title': 'Правление ТСН'})


def tables(request):
    return render(request, "app_core/tables.html", {'menu': menu, 'title': 'Таблицы'})


def charts(request):
    return render(request, "app_core/charts.html", {'menu': menu, 'title': 'Графики'})


def charts_test(request):
    return render(request, "app_core/charts_test.html", {'menu': menu, 'title': 'Графики_TEST'})


def under_construction(request):
    return render(request, 'app_core/under_construction.html', {'menu': menu, 'title': 'Страница в разработке'})
