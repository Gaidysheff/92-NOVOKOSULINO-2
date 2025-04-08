from django.urls import path
from app_core.views import *
from Novokosulino import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('tables/', tables, name='tables'),
    path('charts/', charts, name='charts'),
    path('vote2024/', vote2024, name='vote2024'),
    path('map/', map, name='map'),
    path('management_2024_1/', management_2024_1, name='management_2024_1'),
    path('management_2024_2/', management_2024_2, name='management_2024_2'),
    path('management_2024_3/', management_2024_3, name='management_2024_3'),
    path('achievements/', achievements, name='achievements'),
    path('achieve/<int:pk>/', achieve, name='achieve'),
    path('achievements2025/', achievements2025, name='achievements2025'),
    path('achieve2025/<int:pk>/', achieve2025, name='achieve2025'),
    path('under_construction/', under_construction, name='under_construction'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
