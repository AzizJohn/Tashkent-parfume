from django.db import models
from django.utils.translation import gettext_lazy as _


class RegionChoices(models.TextChoices):
    TASHKENT = "tashkent", _("Tashkent")
    ANDIJAN = "andijan", _("Andijan")
    BUKHARA = "bukhara", _("Bukhara")
    DJIZZAK = "djizzak", _("Djizzak")
    FERGANA = "fergana", _("Fergana")
    KARAKALPAKSTAN = "karakalpakstan", _("Karakalpakstan")
    NAMANGAN = "namangan", _("Namangan")
    NAVOIY = "navoiy", _("Navoiy")
    SAMARQAND = "samarqand", _("Samarqand")
    SIRDARYA = "sirdarya", _("Sirdarya")
    SURKHANDARYA = "surkhandarya", _("Surkhandarya")
    TASHKENT_REGION = "tashkent_region", _("Tashkent Region")
    KHOREZM = "khorezm", _("Khorezm")


class OrderStatusChoices(models.TextChoices):
    ORDER_RECEIVED = "order_received", _("Order Received")
    DURING_DELIVERY = "during_delivery", _("During Delivery")
    DELIVERED = "delivered", _("Delivered")
    CANCELED = "canceled", _("Canceled")


class PaymentMethodChoices(models.TextChoices):
    CASH = "cash", _("Cash")
    CARD = "card", _("Card")
