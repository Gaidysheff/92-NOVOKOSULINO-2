from django.shortcuts import render
from django.conf import settings
from app_news.models import Post
from app_core.models import LoadedFiles


menu = ['на Главную страницу', 'Графики', 'Таблицы']


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Новости',
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


# def file_loading(request):
#     all_files = LoadedFiles.objects.all()

#     context = {
#         'all_files': all_files,
#         'title': 'Загрузка файлов'
#     }

#     if request.POST:
#         # if request.method == 'POST' and request.FILES['myfile']:
#         LoadedFiles.objects.create(
#             text=request.POST.get('text'),
#             file=request.FILES.get('file')
#         )
#     return render(request, 'app_core/files_uploading.html', context)
