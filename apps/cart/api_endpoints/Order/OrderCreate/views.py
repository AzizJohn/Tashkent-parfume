from rest_framework.generics import CreateAPIView

from apps.cart.api_endpoints.Order.OrderCreate.serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = ("OrderCreateAPIView",)
