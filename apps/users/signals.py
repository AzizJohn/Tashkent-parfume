from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.cart.models import Cart
from apps.users.models import User


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

