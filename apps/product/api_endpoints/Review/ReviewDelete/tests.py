from django.urls import reverse
from rest_framework.test import APITestCase

from apps.product.models import Product, Brand, Section, Review
from apps.users.models import User


class ReviewDeleteAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number='+998939999999', password='testpass123',
                                              full_name='Test User')
        self.brand = Brand.objects.create(name='Test Brand')
        self.section = Section.objects.create(name='Test Section')
        self.product = Product.objects.create(name='Test Product', price=10.0, discount_price=5.0, brand=self.brand,
                                              section=self.section)

    def test_delete_review(self):
        Review.objects.create(user=self.user, product=self.product, rating=4, comment='Test comment')
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse("product:ReviewDelete", kwargs={"product_id": self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": 204, "message": "Review deleted from product."})

    # def test_delete_review_unauthorized(self):
    #     # self.client.force_authenticate(user=None)
    #     Review.objects.create(user=self.user, product=self.product, rating=4, comment='Test comment')
    #
    #     response = self.client.delete(reverse("product:ReviewDelete", kwargs={"product_id": self.product.id}))
    #     self.assertEqual(response.status_code, 401)
    #     self.assertEqual(response.data, {"detail": "Authentication credentials were not provided."})
