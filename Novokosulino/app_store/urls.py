from django.urls import path
from app_store.views import *


urlpatterns = [
    path('', archive, name='archive'),
    path('village/', storeNovokosulino, name='archive_Novokosulino'),
    path('image_from_village/<int:pk>', storeNovokosulinoPost, name='image_from_village'),
]
