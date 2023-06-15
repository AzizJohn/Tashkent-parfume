from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.product.models import Product, Section, Brand


class ProductImageBySectionListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Test Brand')
        self.section = Section.objects.create(name='Test Section')
        self.product1 = Product.objects.create(name='Product 1', price=10.0, discount_price=5.0, brand=self.brand,
                                               section=self.section)

    def test_get_product_images_by_section(self):
        section_id = self.section.id
        url = reverse('product:ProductImageListBySection', args=[section_id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
