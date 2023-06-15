from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
            "email": "azizjon1708@gmail.com",
            "phone_number": "+998999999999",
            "full_name": "Azizjon"
        }
        response = self.client.post(reverse("users:auth-create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
