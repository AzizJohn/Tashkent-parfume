from django.urls import reverse
from rest_framework.test import APITestCase

from apps.product.models import Product, Review, Brand, Section
from apps.users.models import User


class ProductListBySectionListAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.brand = Brand.objects.create(name="Test Brand")
        self.section = Section.objects.create(name="Test Section")
        # Create test data for products in the specific section
        self.product1 = Product.objects.create(name="Product 1", price=10, discount_price=5.0, section=self.section,
                                               brand=self.brand)

        # Create test data for reviews for the products in the specific section
        Review.objects.create(user=self.user, product=self.product1, rating=4, comment="Great product!")

    def test_product_list_by_section(self):
        url = reverse('product:ProductListBySection', args=[self.section.id])
        response = self.client.get(url)

        # Assert the status code
        self.assertEqual(response.status_code, 200)
