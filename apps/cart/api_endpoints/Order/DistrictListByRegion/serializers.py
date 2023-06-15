from rest_framework import serializers

from apps.cart.models import District


class DistrictListByRegionSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()

    class Meta:
        model = District
        fields = ('id', 'region', 'name')
