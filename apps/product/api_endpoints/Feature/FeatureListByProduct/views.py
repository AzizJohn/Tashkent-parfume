from rest_framework.generics import ListAPIView

from apps.product.api_endpoints.Feature.FeatureListByProduct.serializers import FeatureListByProductSerializer
from apps.product.models import Feature


class FeatureListByProductAPIView(ListAPIView):
    serializer_class = FeatureListByProductSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("product_id")
        return Feature.objects.filter(product_id=product_id)


__all__ = ['FeatureListByProductAPIView']