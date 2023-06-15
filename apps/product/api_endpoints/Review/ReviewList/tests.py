from apps.users.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.product.models import Review, Brand, Section, Product


class ReviewListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword", full_name="Azizjon")
        self.other_user = User.objects._create_user(phone_number="998999999988", password='otherpassword', full_name='Other User')

        self.brand = Brand.objects.create(name="Test Brand")
        self.section = Section.objects.create(name="Test Section")
        self.product1 = Product.objects.create(name="Test Product 1", price=10.0, discount_price=5.0, brand=self.brand,
                                              section=self.section)
        self.product2 = Product.objects.create(name="Test Product 2", price=10.0, discount_price=5.0, brand=self.brand,
                                               section=self.section)
    def test_get_review_list(self):
        # Create reviews for the authenticated user
        review1 = Review.objects.create(user=self.user, product=self.product1, rating=4, comment='Review 1')
        review2 = Review.objects.create(user=self.user, product=self.product2, rating=5, comment='Review 2')

        # Create reviews for other users
        other_review1 = Review.objects.create(user=self.other_user, product=self.product1, rating=3, comment='Other review 1')
        other_review2 = Review.objects.create(user=self.other_user, product=self.product2, rating=4, comment='Other review 2')

        # Log in the user
        self.client.force_authenticate(user=self.user)

        url = '/api/product/ReviewList/'
        response = self.client.get(reverse("product:ReviewList"))

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

