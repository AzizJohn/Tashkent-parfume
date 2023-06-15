from rest_framework import serializers

from apps.cart.models import CartItem


class CartItemListSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity', 'final_price')
