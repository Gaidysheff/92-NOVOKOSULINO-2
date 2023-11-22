from django.urls import path
from app_news.views import *


urlpatterns = [
    path('', index, name='news'),
    path('post/<int:pk>', post, name='post'),
]
