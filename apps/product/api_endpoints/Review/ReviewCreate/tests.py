from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.product.models import Review, Brand, Section, Product
from apps.users.models import User


class ReviewCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.brand = Brand.objects.create(name="Test Brand")
        self.section = Section.objects.create(name="Test Section")
        self.product = Product.objects.create(name="Test Product 1", price=10.0, discount_price=5.0, brand=self.brand,
                                              section=self.section)

    def test_create_review(self):
        # self.client.force_login(user=self.user)
        self.client.force_authenticate(user=self.user)
        self.client.login(phone_number="+998999999999", password="testpassword", full_name="Azizjon")
        # Send a POST request to create a review
        data = {
            'user': self.user.id,
            'product': self.product.id,
            'rating': 5,
            'comment': 'This is a great product.'
        }

        response = self.client.post(reverse("product:ReviewCreate"), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Review.objects.filter(user=self.user, product=self.product).exists())


    def test_create_duplicate_review(self):
        self.client.force_authenticate(user=self.user)

        # Create a review for the product using the user
        review_data = {
            'user': self.user.id,
            'product': self.product.id,
            'rating': 5,
            'comment': 'This is a great product.'
        }
        response = self.client.post(reverse("product:ReviewCreate"), data=review_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Try to create another review for the same product using the same user
        duplicate_review_data = {
            'user': self.user.id,
            'product': self.product.id,
            'rating': 4,
            'comment': 'This is another review.'
        }
        response = self.client.post(reverse("product:ReviewCreate"), data=duplicate_review_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
