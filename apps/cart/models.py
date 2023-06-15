from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.cart.choices import OrderStatusChoices, PaymentMethodChoices
from apps.common.models import TimeStampedModel
from apps.product.models import Product


class Order(TimeStampedModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name=_("User"))
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, verbose_name=_("Cart"))
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    phone_number = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True)
    additional_phone_number = PhoneNumberField(_("Additional Phone number"), max_length=32, unique=True, null=True)
    # region = models.CharField(max_length=50, choices=RegionChoices.choices, verbose_name=_("Region"))
    region = models.ForeignKey("cart.Region", on_delete=models.CASCADE, verbose_name=_("Region"))
    district = models.ForeignKey("cart.District", on_delete=models.CASCADE, verbose_name=_("District"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    longtitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_("Longtitude"), null=True,
                                     blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_("Latitude"), null=True, blank=True)
    payment_method = models.CharField(max_length=255, choices=PaymentMethodChoices.choices,
                                      verbose_name=_("Payment Method"))
    status = models.CharField(max_length=255, choices=OrderStatusChoices.choices,
                              default=OrderStatusChoices.ORDER_RECEIVED,
                              verbose_name=_("Status"))

    def __str__(self):
        return f"{self.user} - {self.cart} - {self.status}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class Region(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class District(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    # region = models.CharField(max_length=50, choices=RegionChoices.choices, verbose_name=_("Region"))
    region = models.ForeignKey("cart.Region", on_delete=models.CASCADE, verbose_name=_("Region"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")


class Cart(TimeStampedModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name=_("User"))
    total_products = models.PositiveIntegerField(default=0, verbose_name=_("Total Products"))
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Final Price"), default=0)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Discount Price"), blank=True,
                                         null=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Delivery Fee"), default=0)
    in_order = models.BooleanField(default=False, verbose_name=_("In Order"))

    def __str__(self):
        return f"{self.user} - {self.final_price}"

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class CartItem(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, verbose_name=_("Cart"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))
    final_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Final Price"))

    def save(self, *args, **kwargs):
        if self.product.is_discount:
            self.final_price = self.quantity * self.product.discount_price
        else:
            self.final_price = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} - {self.quantity}"

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")


class CartProduct(TimeStampedModel):
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, verbose_name=_("Cart"))
    cart_item = models.ForeignKey("cart.CartItem", on_delete=models.CASCADE, verbose_name=_("Cart Item"))

    def __str__(self):
        return f"{self.cart} - {self.cart_item}"

    class Meta:
        verbose_name = _("Cart Product")
        verbose_name_plural = _("Cart Products")


class Discount(TimeStampedModel):
    min_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                     verbose_name=_("Min Amount"))  # min amount of total price to apply discount
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                          verbose_name=_("Discount Amount"))  # discount amount
    expire_date = models.DateTimeField(verbose_name=_("Expire Date"))

    def __str__(self):
        return f"{self.min_amount} - {self.discount_amount}"

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")


class Cashback(TimeStampedModel):
    cashback_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Cashback Amount"),
                                          blank=True, null=True)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, verbose_name=_("User"))

    def __str__(self):
        return f"{self.user} - {self.cashback_amount}"

    class Meta:
        verbose_name = _("Cashback")
        verbose_name_plural = _("Cashbacks")


class MyCard(TimeStampedModel):
    card_number = models.CharField(max_length=255, verbose_name=_("Card Number"))
    expire_date = models.DateField(verbose_name=_("Expire Date"))
    # cvv = models.CharField(max_length=255, verbose_name=_("CVV"), blank=True, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name=_("User"))

    def __str__(self):
        return f"{self.user} - {self.card_number}"

    class Meta:
        verbose_name = _("My Card")
        verbose_name_plural = _("My Cards")
