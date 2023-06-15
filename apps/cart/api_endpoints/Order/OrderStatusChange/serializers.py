from rest_framework import serializers

from apps.cart.models import Order

class OrderStatusChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status',)