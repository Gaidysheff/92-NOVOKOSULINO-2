from django.contrib import admin
from .models import UploadFilesMultiple


@admin.register(UploadFilesMultiple)
class UploadFilesMultipleAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at', )
    list_display_links = ('id', 'file',)
    search_fields = ('uploaded_at',)
    save_on_top = True
