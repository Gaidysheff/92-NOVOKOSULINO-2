from django.urls import path
from mainapp.views import *
from Novokosulino import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('tables/', tables, name='tables'),
    path('charts/', charts, name='charts'),
    path('management/', management, name='management'),
    # path('uploading/', file_loading, name='uploading'),
    path('under_construction/', under_construction, name='under_construction'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
