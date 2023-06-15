from rest_framework import serializers

from apps.product.models import Product


class ProductImageListBySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image')
