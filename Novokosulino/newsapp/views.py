from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Новости',
    }
    return render(request, "newsapp/index.html", context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    title = post.title
    context = {
        'post': post,
        'title': title,
    }
    return render(request, "newsapp/post.html", context)
