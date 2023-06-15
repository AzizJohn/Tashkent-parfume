from rest_framework.generics import ListAPIView

from apps.cart.api_endpoints.Order.ActiveOrderList.serializers import ActiveOrderListSerializer
from apps.cart.models import Order


class ActiveOrderListAPIView(ListAPIView):
    serializer_class = ActiveOrderListSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(status__in=["order_received", "during_delivery"])


__all__ = ("ActiveOrderListAPIView",)
