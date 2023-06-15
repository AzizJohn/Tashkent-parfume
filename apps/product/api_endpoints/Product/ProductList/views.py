from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView

from apps.product.api_endpoints.Product.ProductList.serializers import ProductListSerializer
from apps.product.models import Product


class ProductFilter(filters.FilterSet):
    brands = filters.CharFilter(field_name="brand__name", method="filter_brands")
    sections = filters.CharFilter(field_name="section__name", method="filter_sections")
    price_from = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_to = filters.NumberFilter(field_name="price", lookup_expr="lte")
    is_discount = filters.BooleanFilter(field_name="is_discount")

    class Meta:
        model = Product
        fields = ["brands", "sections", "price_from", "price_to"]

    def filter_brands(self, queryset, name, value):
        brands = value.split(',')
        return queryset.filter(brand__name__in=brands)

    def filter_sections(self, queryset, name, value):
        sections = value.split(",")
        return queryset.filter(section__name__in=sections)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


__all__ = ['ProductListAPIView']
