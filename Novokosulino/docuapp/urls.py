from django.urls import path
from docuapp.views import *


urlpatterns = [
    path('', documents, name='documents'),
]
