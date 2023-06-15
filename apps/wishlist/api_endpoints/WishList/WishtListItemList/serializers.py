from rest_framework import serializers

from apps.wishlist.models import Wishlist, WishlistItem


class WishlistMiniSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Wishlist
        fields = ("id", "user")


class WishItemlistSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    wishlist = WishlistMiniSerializer()

    class Meta:
        model = WishlistItem
        fields = ("id", "wishlist", "product")
