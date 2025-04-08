from django.shortcuts import render
from app_store.models import *


def archive(request):
    context = {
        'title': 'Разделы фотоархива',
    }
    return render(request, "app_store/main.html", context)


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


def ny2024(request):
    photos = NY2024.objects.all()
    context = {
        'photos': photos,
        'title': 'Празднование Нового 2024 Года',
    }
    return render(request, "app_store/ny2024_index.html", context)


def ny2024Post(request, pk):
    post = NY2024.objects.get(id=pk)
    image = post.uploadedImage
    context = {
        'image': image,
        'title': 'Фото c празднования Нового 2024 Года',
    }
    return render(request, "app_store/ny2024_post.html", context)


def maslenitsa2024(request):
    photos = Maslenitsa2024.objects.all()
    context = {
        'photos': photos,
        'title': 'Празднование Масленицы - 2024 г.',
    }
    return render(request, "app_store/maslenitsa2024_index.html", context)


def maslenitsa2024Post(request, pk):
    post = Maslenitsa2024.objects.get(id=pk)
    image = post.uploadedImage
    context = {
        'image': image,
        'title': 'Фото c празднования Масленицы - 2024 г.',
    }
    return render(request, "app_store/maslenitsa2024_post.html", context)


def ny2025(request):
    photos = NY2025.objects.all()
    context = {
        'photos': photos,
        'title': 'Празднование Нового 2025 Года',
    }
    return render(request, "app_store/ny2025_index.html", context)


def ny2025Post(request, pk):
    post = NY2025.objects.get(id=pk)
    image = post.uploadedImage
    context = {
        'image': image,
        'title': 'Фото c празднования Нового 2025 Года',
    }
    return render(request, "app_store/ny2025_post.html", context)


def maslenitsa2025(request):
    photos = Maslenitsa2025.objects.all()
    context = {
        'photos': photos,
        'title': 'Празднование Масленицы - 2025 г.',
    }
    return render(request, "app_store/maslenitsa2025_index.html", context)


def maslenitsa2025Post(request, pk):
    post = Maslenitsa2025.objects.get(id=pk)
    image = post.uploadedImage
    context = {
        'image': image,
        'title': 'Фото c празднования Масленицы - 2025 г.',
    }
    return render(request, "app_store/maslenitsa2025_post.html", context)
