from rest_framework import serializers

from apps.product.models import Feature


class FeatureListByProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    feature_name = serializers.StringRelatedField()

    class Meta:
        model = Feature
        fields = ("id", "product", "feature_name", "value")
