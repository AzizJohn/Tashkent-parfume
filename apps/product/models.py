from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    image = ImageField(upload_to='product/', blank=True, null=True, verbose_name=_("Image"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    description = RichTextField(verbose_name=_("Description"), null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Discounted Price"))
    is_discount = models.BooleanField(default=False, verbose_name=_("Is Discounted"))
    brand = models.ForeignKey("product.Brand", on_delete=models.CASCADE, verbose_name=_("Brand"))
    section = models.ForeignKey("product.Section", on_delete=models.CASCADE, verbose_name=_("Section"))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_("Quantity"))
    available = models.BooleanField(default=True, verbose_name=_("Available"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Brand(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    icon = ImageField(upload_to='brand/', blank=True, null=True, verbose_name=_("Icon"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class Section(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    icon = ImageField(upload_to='section/', blank=True, null=True, verbose_name=_("Icon"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")


class Review(TimeStampedModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name=_("User"))
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name=_("Product"))
    comment = models.TextField(verbose_name=_("Text"))
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                         verbose_name=_("Rating"), default=0)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rating * '⭐'}"


class Feature(TimeStampedModel):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name=_("Product"))
    feature_name = models.ForeignKey("product.FeatureName", on_delete=models.CASCADE, verbose_name=_("Feature Name"))
    value = models.CharField(max_length=255, verbose_name=_("Value"))

    def __str__(self):
        return f"{self.product} - {self.feature_name} - {self.value}"


class FeatureName(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Feature Name")
        verbose_name_plural = _("Feature Names")
