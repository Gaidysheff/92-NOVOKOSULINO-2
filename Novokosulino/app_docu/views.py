from django.shortcuts import render
from django.conf import settings
from .models import LoadedDocuments
from django.http import HttpResponse, Http404
import os


def documents(request):
    file = LoadedDocuments.objects.all()

    context = {
        "file": file,
        'title': 'Загрузка документов'
    }
    return render(request, "app_docu/documents.html", context)


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
