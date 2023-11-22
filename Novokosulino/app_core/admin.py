from django.contrib import admin
from .models import LoadedFiles


@admin.register(LoadedFiles)
class LoadedFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'file', )
    list_display_links = ('id', 'text',)
    search_fields = ('text',)
    save_on_top = True
