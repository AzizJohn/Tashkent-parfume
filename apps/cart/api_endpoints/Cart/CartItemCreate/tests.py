from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.cart.models import CartItem, Cart, Product
from apps.product.models import Brand, Section
from apps.users.models import User


class CartItemCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.brand = Brand.objects.create(name="Test Brand")
        self.section = Section.objects.create(name="Test Section")
        self.product = Product.objects.create(name="Test Product", price=10.0, discount_price=5.0, brand=self.brand, section=self.section)

    def test_create_cart_item(self):
        self.client.force_authenticate(user=self.user)

        # Send a POST request to create a cart item
        data = {
            'product_id': self.product.id
        }
        response = self.client.post(reverse("cart:CartItemCreate"), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.data['message'], "The product has been added to the cart.")

        # Assert that the cart item is created for the user
        self.assertTrue(CartItem.objects.filter(cart__user=self.user, product=self.product).exists())

    def test_create_cart_item_invalid_product(self):
        self.client.force_authenticate(user=self.user)

        # Send a POST request with an invalid product ID
        data = {
            'product_id': 999  # Invalid product ID
        }
        response = self.client.post(reverse("cart:CartItemCreate"), data=data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Assert that no cart item is created
        self.assertFalse(CartItem.objects.filter(cart__user=self.user).exists())
