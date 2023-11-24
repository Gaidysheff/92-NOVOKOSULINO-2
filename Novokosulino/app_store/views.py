from django.shortcuts import render


def archive(request):
    pass


def storeNovokosulino(request):
    # posts = Post.objects.all()
    context = {
        # 'posts': posts,
        'title': 'История посёлка',
    }
    return render(request, "app_store/village.html", context)
