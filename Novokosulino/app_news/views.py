from django.shortcuts import render
from .models import Post
# from jinja2 import Template


def index(request):
    posts = Post.objects.filter(status='ACT').order_by("order")
    context = {
        'posts': posts,
        # 'title': 'Новости',
    }
    return render(request, "app_news/index.html", context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    title = post.title
    context = {
        'post': post,
        'title': title,
    }
    return render(request, "app_news/post.html", context)
