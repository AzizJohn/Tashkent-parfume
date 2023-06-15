from django.contrib import admin

from apps.cart.models import Order, Region, District, Cart, CartItem, CartProduct, Discount, Cashback, MyCard


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cart', 'region', 'district', 'address', 'phone_number', 'status', 'created_at')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'region', 'district', 'address', 'phone_number', 'status', 'created_at')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'region')


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_products', 'final_price', 'discount_price', 'delivery_fee', 'in_order')
    list_display_links = ('id', 'user')
    search_fields = ('user',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'final_price')
    list_display_links = ('id', 'cart')
    search_fields = ('cart', 'product')


class CartProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'cart_item')
    list_display_links = ('id', 'cart')
    search_fields = ('cart',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_amount', 'discount_amount', 'expire_date')
    list_display_links = ('id', 'expire_date')
    search_fields = ('expire_date', 'discount_amount')


class CashbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cashback_amount')
    list_display_links = ('id', 'user')
    search_fields = ('user',)


class MyCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'card_number', 'expire_date')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'card_number', 'expire_date')


admin.site.register(Order, OrderAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Cashback, CashbackAdmin)
admin.site.register(MyCard, MyCardAdmin)
