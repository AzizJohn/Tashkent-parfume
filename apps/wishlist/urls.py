from django.urls import path

from apps.wishlist.api_endpoints.WishList import WishlistItemCreateAPIView, WishlistItemListAPIView, \
    WishlistItemDeleteAPIView

app_name = "wishlist"

urlpatterns = [
    # Wishlist
    path("WishlistCreate", WishlistItemCreateAPIView.as_view(), name="WishlistCreate"),
    path("Wishlist", WishlistItemListAPIView.as_view(), name="WishlistItemList"),
    path("WishlistItemDelete/<int:product_id>", WishlistItemDeleteAPIView.as_view(), name="WishlistItemDelete"),

]
