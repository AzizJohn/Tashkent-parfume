from django.db import models

from apps.cart.models import CartItem, Discount
from django.utils import timezone

def update_cart(cart):
    cart_data = CartItem.objects.filter(cart=cart).aggregate(models.Sum("final_price"), models.Sum("quantity"))

    if cart_data.get("final_price__sum"):
        cart.final_price = cart_data["final_price__sum"]
    else:
        cart.final_price = 0
    if cart_data.get("quantity__sum"):
        cart.total_products = cart_data["quantity__sum"]
    else:
        cart.total_products = 0
    cart.save()

    discount = Discount.objects.filter(
        min_amount__lte=cart.final_price,
        expire_date__gte=timezone.now()
    ).first()

    if discount:
        cart.final_price = cart.final_price - discount.discount_amount
    else:
        cart.final_price = cart_data["final_price__sum"]

        # Apply cashback if available and requested by the client
    # if use_cashback:     
    #     cashback_amount = cart.user.cashback.cashback_amount if cart.user.cashback else 0
    #     cart.final_price -= cashback_amount
    #     cart.user.cashback.cashback_amount = cart.final_price * 0.05  # Refill cashback with 5% of the final price
    #     cart.user.cashback.save()

    cart.save()