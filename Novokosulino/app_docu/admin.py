from django.contrib import admin
from .models import LoadedDocuments
from django.utils.safestring import mark_safe


@admin.register(LoadedDocuments)
class LoadedDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file_docu', 'get_html_image',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    readonly_fields = ('get_html_image',)
    save_on_top = True

    def get_html_image(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_image.short_description = 'Миниатюра'
