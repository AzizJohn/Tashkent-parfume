# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from apps.cart.models import CartItem
# from apps.product.models import Product, Brand, Section
# from apps.users.models import User
#
#
# class CartItemDeleteFromCartAPIViewTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects._create_user(phone_number="+998999999999", password="testpassword",
#                                               full_name="Azizjon")
#         self.cart = self.user.cart_set.all().first()
#
#
#         self.brand = Brand.objects.create(name="Test Brand")
#         self.section = Section.objects.create(name="Test Section")
#         self.product = Product.objects.create(name="Test Product", price=10.0, discount_price=5.0, brand=self.brand,
#                                               section=self.section)
#
#         # Create a cart item for the product
#         self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product)
#
#
#     def test_delete_cart_item_from_cart(self):
#         self.client.force_authenticate(user=self.user)
#
#         # Send a DELETE request to delete the cart item
#         response = self.client.delete(reverse("cart:CartItemDeleteFromCart", kwargs={"product_id": self.product.id}))
#
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#         # Assert that the cart item is deleted from the database
#         self.assertFalse(CartItem.objects.filter(id=self.cart_item.id).exists())
