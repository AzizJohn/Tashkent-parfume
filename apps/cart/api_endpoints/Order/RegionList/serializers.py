from rest_framework import serializers

from apps.cart.models import Region


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')
