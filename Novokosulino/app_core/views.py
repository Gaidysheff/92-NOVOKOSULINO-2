from django.shortcuts import render
from django.conf import settings
from app_news.models import Post
from app_core.models import Achievements


menu = ['на Главную страницу', 'Графики', 'Таблицы']


def index(request):
    posts = Post.objects.filter(status='ACT').order_by("order")
    context = {
        'posts': posts,
        'title': 'Главная страница',
    }
    return render(request, "app_core/index.html", context)


def achievements(request):
    achieve2024 = Achievements.objects.filter(year='2024').order_by("date")

    context = {
        'achievements2024': achieve2024,
        'title': 'Проведённые мероприятия',
    }
    return render(request, "app_core/achievements.html", context)


def achieve(request, pk):
    post = Achievements.objects.get(id=pk)
    image = post.image
    context = {
        'image': image,
        'title': 'Фото из архива',
    }
    return render(request, "app_core/achieve.html", context)


def management_2024_1(request):
    context = {
        'menu': menu,
        'title': 'Правление ТСН 27.10.23 - 01.07.24 г.'
    }
    return render(request, "app_core/management_2024_1.html", context)


def management_2024_2(request):
    context = {
        'menu': menu,
        'title': 'Правление ТСН  01.07.24 - 04.12.24 г.'
    }
    return render(request, "app_core/management_2024_2.html", context)


def management_2024_3(request):
    context = {
        'menu': menu,
        'title': 'Правление ТСН с 04.12.24 г.'
    }
    return render(request, "app_core/management_2024_3.html", context)


def tables(request):
    return render(request, "app_core/tables.html", {'menu': menu, 'title': 'Таблицы'})


def charts(request):
    return render(request, "app_core/charts.html", {'menu': menu, 'title': 'Графики'})


def vote2024(request):
    return render(request, "app_core/vote2024.html", {'menu': menu, 'title': 'Голосование в 2024 г.'})


def map(request):
    return render(request, "app_core/map.html", {'menu': menu, 'title': 'Карта посёлка'})


def charts_test(request):
    return render(request, "app_core/charts_test.html", {'menu': menu, 'title': 'Графики_TEST'})


def under_construction(request):
    return render(request, 'app_core/under_construction.html', {'menu': menu, 'title': 'Страница в разработке'})
