from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.cart.models import Order, Region, District
from apps.users.models import User
from apps.cart.choices import RegionChoices

class ActiveOrderListAPIView(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.cart = self.user.cart_set.all().first()
        self.region = Region.objects.create(name=RegionChoices.TASHKENT)
        self.district = District.objects.create(name="Mirzo Ulugbek", region=self.region)
        self.order1 = Order.objects.create(user=self.user, cart=self.cart, first_name="Azizjon", last_name="Eshpulatov",
                                           region=self.region, district=self.district, address="35-71",
                                           payment_method="Cash", status="order_received")
        self.order2 = Order.objects.create(user=self.user, cart=self.cart, first_name="Azizjon", last_name="Eshpulatov",
                                           region=self.region, district=self.district, address="35-71",
                                           payment_method="Cash", status="during_delivery")

    def test_active_order_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("cart:ActiveOrderList"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
