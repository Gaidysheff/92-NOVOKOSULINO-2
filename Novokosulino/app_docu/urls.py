from django.urls import path
from app_docu.views import *


urlpatterns = [
    path('', documents, name='documents'),
]
