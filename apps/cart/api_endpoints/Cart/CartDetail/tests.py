from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class CartDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")


    def test_get_cart_detail(self):
        self.client.force_authenticate(user=self.user)

        # Send a GET request to retrieve the cart detail
        response = self.client.get(reverse("cart:CartDetail"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cart_detail_unauthenticated(self):
        # Send a GET request to retrieve the cart detail without authentication
        response = self.client.get(reverse("cart:CartDetail"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
