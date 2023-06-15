from rest_framework import serializers

from apps.cart.models import Order, Cart


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('cart', 'first_name', 'last_name', 'phone_number', 'additional_phone_number', 'region', 'district', 'address',
                  'payment_method')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        cart = validated_data['cart']
        try:
            cart = Cart.objects.get(id=cart.id, user=user)

        except Cart.DoesNotExist:
            raise serializers.ValidationError("Cart does not exist")

        if cart.in_order != False:
            raise serializers.ValidationError("Cart is already in order")

        cart.in_order = True
        cart.save()

        Cart.objects.create(user=user, in_order=False)

        return super().create(validated_data)
