from rest_framework import serializers

from apps.cart.models import Cart


class CartDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'total_products', 'final_price', 'delivery_fee')
