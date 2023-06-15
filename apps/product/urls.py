from django.urls import path

from apps.product.api_endpoints.Brand import BrandListAPIView
from apps.product.api_endpoints.Feature import FeatureListByProductAPIView
from apps.product.api_endpoints.Product import ProductListAPIView, ProductListBySectionListAPIView, \
    NewProductsListAPIView, ProductImageBySectionListAPIView
from apps.product.api_endpoints.Review import ReviewCreateAPIView, ReviewDeleteAPIView, ReviewListAPIView
from apps.product.api_endpoints.Section import SectionListAPIView

app_name = "product"

urlpatterns = [
    # Brand
    path("BrandList", BrandListAPIView.as_view(), name="BrandList"),

    # Section
    path("SectionList", SectionListAPIView.as_view(), name="SectionList"),

    # Product
    path("ProductList", ProductListAPIView.as_view(), name="ProductList"),
    path("ProductListBySection/<int:section_id>", ProductListBySectionListAPIView.as_view(),
         name="ProductListBySection"),
    path("NewProductsList", NewProductsListAPIView.as_view(), name="NewProductsList"),
    path("ProductImageListBySection/<int:section_id>", ProductImageBySectionListAPIView.as_view(), name="ProductImageListBySection"),

    # Review
    path("ReviewCreate", ReviewCreateAPIView.as_view(), name="ReviewCreate"),
    path("ReviewDelete/<int:product_id>", ReviewDeleteAPIView.as_view(), name="ReviewDelete"),
    path("ReviewList", ReviewListAPIView.as_view(), name="ReviewList"),

    # Feature
    path("FeatureListByProduct/<int:product_id>", FeatureListByProductAPIView.as_view(), name="FeatureListByProduct"),

]
