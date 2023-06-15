from rest_framework import serializers

from apps.product.models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('id', 'user', 'product', 'comment', 'rating', 'created_at')
