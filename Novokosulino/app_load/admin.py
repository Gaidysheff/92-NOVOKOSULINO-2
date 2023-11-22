from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploadedFile', 'dateTimeOfUpload', )
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    save_on_top = True
