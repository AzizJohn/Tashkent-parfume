from rest_framework import serializers

from apps.wishlist.models import WishlistItem, Wishlist
from apps.wishlist.utils import get_session_key


class WishlistItemCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ("id", "product")
        # read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        request = self.context['request']

        def get_or_create_wishlist(request):
            if request.user.is_authenticated:
                try:
                    wishlist = Wishlist.objects.get(session_key=get_session_key(request))
                    wishlist.user = request.user
                    wishlist.save()
                except:
                    wishlist = Wishlist.objects.create(user=request.user, session_key=get_session_key(request))

            else:
                wishlist, _ = Wishlist.objects.get_or_create(session_key=get_session_key(request))
            return wishlist

        wishlist = get_or_create_wishlist(request)

        validated_data['wishlist'] = wishlist

        wishlist_item = WishlistItem.objects.create(**validated_data)

        return wishlist_item
