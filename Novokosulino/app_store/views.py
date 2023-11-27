from django.shortcuts import render
from .models import NovokosulinoArchive


def archive(request):
    pass


def storeNovokosulino(request):
    posts = NovokosulinoArchive.objects.filter(year='2015').order_by("order")
    context = {
        'posts': posts,
        'title': 'История посёлка',
    }
    return render(request, "app_store/village.html", context)
