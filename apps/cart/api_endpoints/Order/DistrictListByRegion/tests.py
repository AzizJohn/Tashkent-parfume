from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.cart.choices import RegionChoices
from apps.users.models import User
from apps.cart.models import Region, District

class DistrictListByRegionAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.region = Region.objects.create(name=RegionChoices.TASHKENT)
        self.district = District.objects.create(name="Mirzo Ulugbek", region=self.region)

    def test_get_district_list_by_region(self):
        self.client.force_authenticate(user=self.user)

        # Send a GET request to retrieve the district list by region
        response = self.client.get(reverse("cart:DistrictListByRegion", kwargs={"region_id": self.region.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

