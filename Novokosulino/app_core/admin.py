from django.contrib import admin
from .models import Achievements
from django.utils.safestring import mark_safe


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    fields = ['year', 'date', 'text', 'image', 'icon', ]
    readonly_fields = ['icon_image',]
    list_display = [
        'id', 'year', 'date', 'icon_image', 'text', 'image', 'icon', ]
    list_display_links = ['id', 'year', 'date', 'text', ]
    save_on_top = True

    @admin.display(description="Фото")
    def icon_image(self, item: Achievements):
        if item.icon:
            return mark_safe(f"<img src='{item.icon.url}' width=100>")
        return "Без фото"
