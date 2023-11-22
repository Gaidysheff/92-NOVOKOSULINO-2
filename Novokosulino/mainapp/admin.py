from django.contrib import admin
from .models import LoadedFiles, LoadedDocuments


@admin.register(LoadedFiles)
class LoadedFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'file', )
    list_display_links = ('id', 'text',)
    search_fields = ('text',)
    save_on_top = True


@admin.register(LoadedDocuments)
class LoadedDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file_docu', )
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    save_on_top = True
