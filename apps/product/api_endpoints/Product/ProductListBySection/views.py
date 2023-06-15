from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.product.api_endpoints.Product.ProductListBySection.serializers import ProductListBySectionSerializer
from apps.product.models import Product


class ProductListBySectionListAPIView(ListAPIView):
    serializer_class = ProductListBySectionSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        products = Product.objects.filter(section=self.kwargs['section_id'])

        # brand_ids = [product.brand.id for product in products]
        # brands = Brand.objects.filter(id__in=brand_ids)
        return products
