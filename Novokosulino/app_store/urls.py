from django.urls import path
from app_store.views import *


urlpatterns = [
    path('', archive, name='archive'),
    path('village/', storeNovokosulino, name='archive_Novokosulino'),
    path('image_from_village/<int:pk>/',
         storeNovokosulinoPost, name='image_from_village'),
    path('ny2024/', ny2024, name='ny2024'),
    path('ny2024/<int:pk>/', ny2024Post, name='image_from_ny2024'),
    path('ny2025/', ny2025, name='ny2025'),
    path('ny2025/<int:pk>/', ny2025Post, name='image_from_ny2025'),
    path('maslenitsa2024/', maslenitsa2024, name='maslenitsa2024'),
    path(
        'maslenitsa2024/<int:pk>/',
        maslenitsa2024Post,
        name='image_from_maslenitsa2024'
    ),
]
