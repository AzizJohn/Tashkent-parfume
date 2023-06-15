from rest_framework.generics import ListAPIView

from apps.cart.api_endpoints.Order.OrderHistoryList.serializers import OrderHistoryListSerializer
from apps.cart.models import Order


class OrderHistoryListAPIView(ListAPIView):
    serializer_class = OrderHistoryListSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user.id, status__in=["delivered", "canceled"])


__all__ = ("OrderHistoryListAPIView",)
