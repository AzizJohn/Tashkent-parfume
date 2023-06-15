from rest_framework import serializers

from apps.product.models import Section


class SectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'icon')
