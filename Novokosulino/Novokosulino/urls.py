from django.contrib import admin
from django.urls import include, path, re_path
from . import settings
from django.conf.urls.static import static
from django.views.static import serve
from mainapp.views import document


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('news/', include('newsapp.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    re_path(r'^download/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    path('docu/', document, name='document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
