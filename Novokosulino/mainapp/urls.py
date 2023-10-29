from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('', index, name='home'),
    path('tables/', tables, name='tables'),
    path('charts/', charts, name='charts'),
    path('under_construction/', under_construction, name='under_construction'),
]
