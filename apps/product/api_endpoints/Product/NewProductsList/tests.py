from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.product.models import Product, Review, Brand, Section
from apps.users.models import User


class NewProductsListAPITestCase(APITestCase):
    def setUp(self):
        # Create test products with reviews
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.brand = Brand.objects.create(name="Test Brand")
        self.section = Section.objects.create(name="Test Section")
        self.product1 = Product.objects.create(name="Test Product 1", price=10.0, discount_price=5.0, brand=self.brand,
                                               section=self.section)
        Review.objects.create(user=self.user, product=self.product1, rating=4, comment="Great product!")
        Review.objects.create(user=self.user, product=self.product1, rating=5, comment="Excellent product!")

        self.url = reverse("product:NewProductsList")

    def test_get_new_products_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
