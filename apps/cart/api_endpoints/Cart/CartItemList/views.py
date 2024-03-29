from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CartItemListSerializer

from apps.cart.models import Cart, CartItem


class CartItemListAPIView(ListAPIView):
    serializer_class = CartItemListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user, in_order=False).first()
        products = CartItem.objects.filter(cart=cart)
        return products