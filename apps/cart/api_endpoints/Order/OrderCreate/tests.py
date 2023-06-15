from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.cart.choices import RegionChoices
from apps.cart.models import Region, District
from apps.users.models import User


class OrderCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.cart = self.user.cart_set.all().first()
        self.region = Region.objects.create(name=RegionChoices.TASHKENT)
        self.district = District.objects.create(name="Mirzo Ulugbek", region=self.region)

    def test_order_create(self):
        self.client.force_authenticate(user=self.user)

        data = {
            # "user": self.user,
            "cart": self.cart.id,
            "first_name": "Azizjon",
            "last_name": "Eshpulatov",
            "phone_number": "+998999999999",
            "additional_phone_number": "+998999999999",
            "region": self.region.id,
            "district": self.district.id,
            "address": "35-71",
            "payment_method": "cash",

        }

        # Send a POST request to create an order
        response = self.client.post(reverse("cart:OrderCreate"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
