from django.urls import path
from app_store.views import *


urlpatterns = [
    path('', archive, name='archive'),
    path('village/', storeNovokosulino, name='archive_Novokosulino'),
    path('image_from_village/<int:pk>/',
         storeNovokosulinoPost, name='image_from_village'),
    path('ny2024/', ny2024, name='ny2024'),
    path('ny2024/<int:pk>/', ny2024Post, name='image_from_ny2024'),
]
