from django.urls import path
from app_docu.views import *


urlpatterns = [
    path('', documents, name='documents'),
    path('<int:docu_id>/', document, name='document'),
]
