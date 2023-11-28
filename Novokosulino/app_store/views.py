from django.shortcuts import render
from .models import NovokosulinoArchive


def archive(request):
    pass


def storeNovokosulino(request):
    posts15 = NovokosulinoArchive.objects.filter(year='2015').order_by("order")
    posts16 = NovokosulinoArchive.objects.filter(year='2016').order_by("order")
    posts17 = NovokosulinoArchive.objects.filter(year='2017').order_by("order")
    posts18 = NovokosulinoArchive.objects.filter(year='2018').order_by("order")
    posts19 = NovokosulinoArchive.objects.filter(year='2019').order_by("order")
    # posts20 = NovokosulinoArchive.objects.filter(year='2020').order_by("order")
    # posts21 = NovokosulinoArchive.objects.filter(year='2021').order_by("order")
    # posts22 = NovokosulinoArchive.objects.filter(year='2022').order_by("order")
    # posts23 = NovokosulinoArchive.objects.filter(year='2023').order_by("order")
    # posts24 = NovokosulinoArchive.objects.filter(year='2024').order_by("order")
    context = {
        'posts15': posts15,
        'posts16': posts16,
        'posts17': posts17,
        'posts18': posts18,
        'posts19': posts19,
        # 'posts20': posts20,
        # 'posts21': posts21,
        # 'posts22': posts22,
        # 'posts23': posts23,
        # 'posts24': posts24,
        'title': 'История посёлка',
    }
    return render(request, "app_store/village_index.html", context)

def storeNovokosulinoPost(request, pk):
    post = NovokosulinoArchive.objects.get(id=pk)
    image = post.uploadedImage
    context = {
        'image': image,
        'title': 'Фото из архива',
    }
    return render(request, "app_store/village_post.html", context)
