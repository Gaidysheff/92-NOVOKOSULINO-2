from django.urls import path
from app_core.views import *
from Novokosulino import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('tables/', tables, name='tables'),
    path('charts/', charts, name='charts'),
    path('map/', map, name='map'),
    path('management/', management, name='management'),
    path('achievements/', achievements, name='achievements'),
    path('achieve/<int:pk>/', achieve, name='achieve'),
    path('under_construction/', under_construction, name='under_construction'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
