from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")

    def test_login(self):
        data = {
            "phone_number": "+998999999999",
            "password": "testpassword",

        }

        response = self.client.post(reverse("users:auth-login"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
