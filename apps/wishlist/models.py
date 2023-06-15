from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Wishlist(TimeStampedModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, verbose_name=_("User"), null=True, blank=True)
    session_key = models.CharField(max_length=255, verbose_name=_("Session Key"), null=True, blank=True, unique=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("WishList")
        verbose_name_plural = _("Wishlists")


class WishlistItem(TimeStampedModel):
    wishlist = models.ForeignKey("wishlist.WishList", on_delete=models.CASCADE, verbose_name=_("WishList"))
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name=_("Product"))

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _("WishList Item")
        verbose_name_plural = _("WishList Items")
        unique_together = ("wishlist", "product")
