from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.wishlist.api_endpoints.WishList.WishtListItemList.serializers import WishItemlistSerializer
from apps.wishlist.models import WishlistItem


class WishlistItemListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishItemlistSerializer

    def get_queryset(self):
        return WishlistItem.objects.filter(wishlist__user=self.request.user)


__all__ = ["WishlistItemListAPIView"]