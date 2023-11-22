from django.urls import path
from app_load.views import *


urlpatterns = [
    path('', uploadFile, name='upload'),
]
