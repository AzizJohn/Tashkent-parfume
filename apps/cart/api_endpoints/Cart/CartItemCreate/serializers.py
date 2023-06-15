from django.http import Http404
from rest_framework import serializers

from apps.cart.models import CartItem, Cart, Product
from apps.cart.utils import update_cart


class CartItemCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ("product_id",)

    def create(self, validated_data):

        try:
            product = Product.objects.get(id=validated_data["product_id"])
        except Product.DoesNotExist:
            raise Http404("Product not found")

        user = self.context["request"].user

        cart = Cart.objects.filter(user=user, in_order=False).first()

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )

        update_cart(cart=cart)

        return cart_item