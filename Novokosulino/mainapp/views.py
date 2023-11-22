from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
from django.conf import settings
from newsapp.models import Post
from mainapp.models import LoadedFiles, LoadedDocuments
from django.http import HttpResponse, Http404
import os


menu = ['на Главную страницу', 'Графики', 'Таблицы']


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Новости',
    }
    return render(request, "mainapp/index.html", context)


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


def file_loading(request):
    all_files = LoadedFiles.objects.all()

    context = {
        'all_files': all_files,
        'title': 'Загрузка файлов'
    }

    if request.POST:
        # if request.method == 'POST' and request.FILES['myfile']:
        LoadedFiles.objects.create(
            text=request.POST.get('text'),
            file=request.FILES.get('file')
        )
    return render(request, 'mainapp/files_uploading.html', context)


def document(request):
    file = LoadedDocuments.objects.all()

    context = {
        "file": file,
        'title': 'Загрузка документов'
    }
    return render(request, "mainapp/documents.html", context)


def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, "rb") as fh:
            response = HttpResponse(
                fh.read(), content_type="application/file_docu")
            response["Content-Disposition"] = "inline; filename=" + os.path.basename(
                download_path
            )
            return response
    raise Http404
