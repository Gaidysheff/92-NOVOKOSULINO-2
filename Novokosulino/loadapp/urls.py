from django.urls import path
from loadapp.views import *


urlpatterns = [
    path('', uploadFile, name='upload'),
]
