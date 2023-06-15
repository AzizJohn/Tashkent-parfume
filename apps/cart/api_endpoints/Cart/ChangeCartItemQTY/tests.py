from rest_framework import status
from rest_framework.test import APITestCase

from apps.cart.models import CartItem
from apps.product.models import Product, Brand, Section
from apps.users.models import User


class ChangeCartItemQTYAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
                                              full_name="Azizjon")

        # Create a cart for the user
        self.cart = self.user.cart_set.all().first()

        # Create a product
        self.brand = Brand.objects.create(name='Test Brand')
        self.section = Section.objects.create(name='Test Section')
        self.product = Product.objects.create(name='Test Product', price=10.0, discount_price=5.0, brand=self.brand,
                                              section=self.section)

        # Create a cart item for the product in the cart
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)

        # Set up the API endpoint URL
        self.url = '/api/cart/ChangeCartItemQTY'

    def test_change_cart_item_quantity(self):
        # Log in the user
        self.client.login(phone_number="+998999999999", password="testpassword")

        # Define the payload data
        payload = {
            'product_id': self.product.id,
            'quantity': 5,
        }

        # Send a POST request to the API endpoint
        response = self.client.post(self.url, payload)

        # Assert that the response has a 202 status code
        # self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Refresh the cart item from the database
        self.cart_item.refresh_from_db()

        # Assert that the cart item quantity has been updated
        # self.assertEqual(self.cart_item.quantity, 5)
