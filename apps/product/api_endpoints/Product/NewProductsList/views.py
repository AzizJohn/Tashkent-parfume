from rest_framework.generics import ListAPIView

from apps.product.api_endpoints.Product.NewProductsList.serializers import NewProductsSerializer
from apps.product.models import Product


class NewProductsListAPIView(ListAPIView):
    serializer_class = NewProductsSerializer
    queryset = Product.objects.all().order_by("-created_at")[:10]


__all__ = ['NewProductsListAPIView']
