from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.product.models import Brand


class BrandListAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse("product:BrandList")
        self.brand1 = Brand.objects.create(name="Brand 1", icon="icon1.png")
        self.brand2 = Brand.objects.create(name="Brand 2", icon="icon2.png")

    def test_get_brand_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
