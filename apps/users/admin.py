from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'full_name', 'get_html_photo', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'phone_number', 'full_name')
    search_fields = ('phone_number', 'full_name')

    def get_html_photo(self, object):
        if object.profile_image:
            return mark_safe(f"<img src='{object.profile_image.url}' width=50>")

    get_html_photo.short_description = "profile_image"


admin.site.register(User, UserAdmin)

