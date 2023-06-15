from rest_framework.generics import ListAPIView

from apps.product.api_endpoints.Product.ProductImageListBySection.serializers import ProductImageListBySectionSerializer
from apps.product.models import Product


class ProductImageBySectionListAPIView(ListAPIView):
    serializer_class = ProductImageListBySectionSerializer

    def get_queryset(self):
        section_id = self.kwargs.get("section_id")
        return Product.objects.filter(section_id=section_id)


__all__ = ['ProductImageBySectionListAPIView']