from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.product.models import Feature, Product, Brand, Section, FeatureName


class FeatureListByProductAPITestCase(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="Brand 1", )
        self.section = Section.objects.create(name="Section 1", )
        self.product = Product.objects.create(name="Product 1", price=100, discount_price=50, brand=self.brand,
                                              section=self.section)
        self.featurename = FeatureName.objects.create(name="Feature 1", )
        self.feature1 = Feature.objects.create(product=self.product, feature_name=self.featurename, value="Value 1")
        self.url = reverse("product:FeatureListByProduct", args=[self.product.id])

    def test_get_feature_list_by_product(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

