from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.cart.models import Cart, CartItem
from apps.product.models import Product, Brand, Section
from apps.users.models import User


class CartItemListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")
        self.cart = self.user.cart_set.all().first()
        self.brand = Brand.objects.create(name="Test Brand")
        self.section = Section.objects.create(name="Test Section")
        self.product = Product.objects.create(name="Test Product", price=10.0, discount_price=5.0, brand=self.brand, section=self.section)

        # Create a cart item for the product
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product)

    def test_get_cart_item_list(self):
        self.client.force_authenticate(user=self.user)

        # Send a GET request to retrieve the cart item list
        response = self.client.get(reverse("cart:CartItemList"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

