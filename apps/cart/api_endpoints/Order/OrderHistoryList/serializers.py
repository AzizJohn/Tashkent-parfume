from rest_framework import serializers

from apps.cart.models import Order, Cart


class CartMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("id", "total_products", "final_price", "delivery_fee")


class OrderHistoryListSerializer(serializers.ModelSerializer):
    cart = CartMiniSerializer()

    class Meta:
        model = Order
        fields = ("id", "cart", "status", "created_at")
