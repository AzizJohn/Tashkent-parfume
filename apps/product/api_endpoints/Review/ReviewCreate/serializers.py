from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.product.models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        # fields = ('product', 'rating', 'comment')
        fields = ('user', 'product', 'rating', 'comment')

    def create(self, validated_data):
        # print(validated_data)
        if Review.objects.filter(user=validated_data["user"], product=validated_data["product"]).exists():
            raise serializers.ValidationError(detail={"comment": _("You can't comment twice")}, code="unique")
        return super().create(validated_data)
