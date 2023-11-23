from django.urls import path
from app_load_multiple.views import *


urlpatterns = [
    path('', upload_and_display_files, name='upload_and_display'),
]
