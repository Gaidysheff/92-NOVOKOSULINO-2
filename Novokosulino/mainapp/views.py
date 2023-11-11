from django.shortcuts import render


menu = ['на Главную страницу', 'Графики', 'Таблицы']


def index(request):
    return render(request, "mainapp/index.html", {'menu': menu, 'title': 'Главная страница'})


def management(request):
    return render(request, "mainapp/management.html", {'menu': menu, 'title': 'Правление ТСН'})


def tables(request):
    return render(request, "mainapp/tables.html", {'menu': menu, 'title': 'Таблицы'})


def charts(request):
    return render(request, "mainapp/charts.html", {'menu': menu, 'title': 'Графики'})


def charts_test(request):
    return render(request, "mainapp/charts_test.html", {'menu': menu, 'title': 'Графики_TEST'})


def under_construction(request):
    return render(request, 'mainapp/under_construction.html', {'menu': menu, 'title': 'Страница в разработке'})
