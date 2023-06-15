from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.cart.models import Region


class RegionListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.region1 = Region.objects.create(name="region1")
        self.region2 = Region.objects.create(name="region2")
        self.region3 = Region.objects.create(name="region3")

    def test_region_list(self):
        response = self.client.get(reverse("cart:RegionList"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
