from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.wishlist.models import WishlistItem


class WishlistItemDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishlistItem.objects.all()

    def destroy(self, request, *args, **kwargs):

        try:
            product = WishlistItem.objects.get(wishlist__user=self.request.user, product=self.kwargs['product_id'])
            product.delete()
            return Response({"status": 204, "message": "Product removed from wishlist."})
        except ObjectDoesNotExist:
            raise Http404("Product not found")


__all__ = ["WishlistItemDeleteAPIView"]
