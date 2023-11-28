from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'dateCreation', 'title', 'overview', 'text', 'status', 'order',
                    'get_html_picture', )
    list_display_links = ('id', 'title', 'overview',
                          'text', 'get_html_picture',)
    list_editable = ('status', 'order',)
    search_fields = ('title', 'text',)
    list_filter = ('dateCreation', 'status',)
    readonly_fields = ('id', 'dateCreation', 'get_html_picture',)
    save_on_top = True

    def get_html_picture(self, object):
        if object.picture:
            return mark_safe(f'<img src="{object.picture.url}" width=70')

    get_html_picture.short_description = "Миниатюра"

  