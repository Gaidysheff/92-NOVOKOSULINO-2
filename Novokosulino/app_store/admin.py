from django.contrib import admin
from .models import NovokosulinoArchive
from django.utils.safestring import mark_safe


@admin.register(NovokosulinoArchive)
class NovokosulinoArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'text', 'uploadedImage',
                    'dateOfUpload', 'get_html_image', )
    list_display_links = ('id', 'year', 'text',
                          'uploadedImage', 'get_html_image',)
    search_fields = ('text',)
    list_filter = ('year',)
    readonly_fields = ('id', 'dateOfUpload', 'get_html_image',)
    save_on_top = True

    def get_html_image(self, object):
        if object.uploadedImage:
            return mark_safe(f'<img src="{object.uploadedImage.url}" width=70')

    get_html_image.short_description = "Миниатюра"
