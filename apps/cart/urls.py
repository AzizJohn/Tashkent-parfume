from django.urls import path

from apps.cart.api_endpoints.Cart import CartDetailAPIView, CartItemCreateAPIView, CartItemDeleteFromCartAPIView, \
    CartItemListAPIView, ChangeCartItemQTYAPIView
from apps.cart.api_endpoints.Order import RegionListAPIView, DistrictListByRegionAPIView, OrderCreateAPIView, \
    OrderStatusChangeAPIView, OrderHistoryListAPIView, ActiveOrderListAPIView

app_name = "cart"

urlpatterns = [
    # Cart
    path("CartDetail", CartDetailAPIView.as_view(), name="CartDetail"),
    path("CartItemCreate", CartItemCreateAPIView.as_view(), name="CartItemCreate"),
    path("CartItemDeleteFromCart/<int:product_id>", CartItemDeleteFromCartAPIView.as_view(),
         name="CartItemDeleteFromCart"),
    path("CartItemList", CartItemListAPIView.as_view(), name="CartItemList"),
    path("ChangeCartItemQTY", ChangeCartItemQTYAPIView.as_view(), name="ChangeCartItemQTY"),
    # Order
    path("RegionList", RegionListAPIView.as_view(), name="RegionList"),
    path("DistrictListByRegion/<int:region_id>", DistrictListByRegionAPIView.as_view(), name="DistrictListByRegion"),
    path("OrderCreate", OrderCreateAPIView.as_view(), name="OrderCreate"),
    path("OrderStatusChange/<int:pk>", OrderStatusChangeAPIView.as_view(), name="OrderStatusChange"),
    path("OrderHistoryList", OrderHistoryListAPIView.as_view(), name="OrderHistoryList"),
    path("ActiveOrderList", ActiveOrderListAPIView.as_view(), name="ActiveOrderList"),

]
