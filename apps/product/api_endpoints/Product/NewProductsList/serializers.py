from django.db.models import Sum
from rest_framework import serializers

from apps.product.models import Product, Review


class NewProductsSerializer(serializers.ModelSerializer):
    product_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'product_rating', 'is_discount', 'discount_price')

    def get_product_rating(self, obj):
        count_rating_number = Review.objects.filter(product=obj).count()
        sum_rating_number = Review.objects.filter(product=obj).aggregate(Sum('rating'))['rating__sum']

        if sum_rating_number is None:
            sum_rating_number = 0

        if count_rating_number is None:
            count_rating_number = 0

        try:
            rating = sum_rating_number / count_rating_number
        except ZeroDivisionError:
            rating = 0

        rating = round(rating, 1)

        return rating