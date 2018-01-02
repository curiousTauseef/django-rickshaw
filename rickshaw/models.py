from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


# Managers

class Wheels(models.Manager):
    pass


class CargoHold(models.Manager):
    pass


# Models

class Rickshaw(models.Model):
    uuid = models.UUIDField(verbose_name=_('UUID'), unique=True, default=uuid4, editable=False)
    driver = models.ForeignKey(settings.RICKSHAW_USER_MODEL, on_delete=models.CASCADE, to_field="id", blank=True, null=True, verbose_name=_('Driver'))
    session = models.CharField(max_length=2000, blank=True, null=True, unique=True)
    paid = models.BooleanField(default=False, verbose_name=_('Paid'))
    saved = models.BooleanField(default=False, verbose_name=_('Saved'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    wheels = Wheels()

    def __str__(self):
        return self.uuid.__str__()

    class Meta:
        db_table = "rickshaw_rickshaw_table"
        verbose_name = "Rickshaw"
        verbose_name_plural = "Rickshaws"


class Cargo(models.Model):
    uuid = models.UUIDField(_('UUID'), unique=True, default=uuid4, editable=False)
    rickshaw = models.ForeignKey(Rickshaw, on_delete=models.CASCADE, to_field="uuid", verbose_name=_('Rickshaw'))
    product = models.ForeignKey(settings.RICKSHAW_PRODUCT_MODEL, on_delete=None, to_field="id", verbose_name=_('Product'))
    quantity = models.IntegerField(default=1, verbose_name=_('Quantity'))
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, verbose_name=_('Price'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    hold = CargoHold()

    class Meta:
        db_table = "rickshaw_cargo_table"
        verbose_name = "Rickshaw Cargo"
        verbose_name_plural = "Rickshaw Cargoes"
