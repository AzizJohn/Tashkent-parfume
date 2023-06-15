from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.wishlist.api_endpoints.WishList.WishListItemCreate.serializers import WishlistItemCreateSerializers
from apps.wishlist.models import WishlistItem, Wishlist
from apps.wishlist.utils import get_session_key


class WishlistItemCreateAPIView(CreateAPIView):
    serializer_class = WishlistItemCreateSerializers
    queryset = WishlistItem.objects.all()

    """
        Create a wishlistitem with authenticated user or session_key.
        """

    # def create(self, request, *args, **kwargs):
    #
    #     def get_or_create_wishlist(request):
    #         if request.user.is_authenticated:
    #             wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    #         else:
    #             wishlist, _ = Wishlist.objects.get_or_create(session_key=get_session_key(request))
    #         return wishlist
    #     wishlist = get_or_create_wishlist(request)
    #
    #     data = request.data
    #     data['wishlist'] = wishlist
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ['WishlistItemCreateAPIView']
