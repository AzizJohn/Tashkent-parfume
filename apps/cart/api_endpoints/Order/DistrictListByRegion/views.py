from rest_framework.generics import ListAPIView

from apps.cart.api_endpoints.Order.DistrictListByRegion.serializers import DistrictListByRegionSerializer
from apps.cart.models import District


class DistrictListByRegionAPIView(ListAPIView):
    serializer_class = DistrictListByRegionSerializer

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return District.objects.filter(region_id=region_id)


__all__ = ("DistrictListByRegionAPIView",)
