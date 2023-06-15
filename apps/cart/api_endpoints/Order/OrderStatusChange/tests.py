from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.cart.models import Order, Region, District
from apps.users.models import User


class OrderStatusChangeAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.cart = self.user.cart_set.all().first()

        self.region = Region.objects.create(name="Tashkent")
        self.district = District.objects.create(name="Mirzo Ulugbek", region=self.region)
        self.order1 = Order.objects.create(user=self.user, cart=self.cart, first_name="Azizjon", last_name="Eshpulatov",
                                           region=self.region, district=self.district, address="35-71",
                                           payment_method="Cash", status="order_received")
        self.order2 = Order.objects.create(user=self.user, cart=self.cart, first_name="Azizjon", last_name="Eshpulatov",
                                           region=self.region, district=self.district, address="35-71",
                                           payment_method="Cash", status="during_delivery")

    def test_order_status_change(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "status": "delivered"
        }

        response = self.client.put(reverse("cart:OrderStatusChange", kwargs={"pk": self.order1.pk}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("status"), "delivered")
