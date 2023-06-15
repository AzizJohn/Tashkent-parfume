from rest_framework.generics import ListAPIView

from apps.cart.api_endpoints.Order.RegionList.serializers import RegionListSerializer
from apps.cart.models import Region


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer


__all__ = ["RegionListAPIView"]
