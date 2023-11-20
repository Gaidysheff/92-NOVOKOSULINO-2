from django.urls import path
from newsapp.views import *


urlpatterns = [
    path('', index, name='news'),
    path('post/<int:pk>', post, name='post'),
]
