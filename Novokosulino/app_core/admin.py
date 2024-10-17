from django.contrib import admin
from .models import Achievements
from django.utils.safestring import mark_safe


admin.site.register(Achievements)
