from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.cart.api_endpoints.Order.OrderStatusChange.serializers import OrderStatusChangeSerializer
from apps.cart.models import Order


class OrderStatusChangeAPIView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusChangeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ("OrderStatusChangeAPIView",)
