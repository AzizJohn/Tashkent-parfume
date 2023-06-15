from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from apps.product.models import Product, Brand, Section, Review, Feature, FeatureName


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'price', 'is_discount', 'discount_price', 'available', 'quantity')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = "image"


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def get_html_photo(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_photo.short_description = "icon"


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def get_html_photo(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_photo.short_description = "icon"


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating')
    list_display_links = ('id', 'user', 'product')
    search_fields = ('user', 'product')


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'feature_name', 'value')
    list_display_links = ('id', 'product')
    search_fields = ('product', 'feature_name')


class FeatureNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(FeatureName, FeatureNameAdmin)

