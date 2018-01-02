from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from .models import Cargo, Rickshaw
from .errors import RickshawCargoError


@receiver(post_save, sender=Rickshaw)
def store_rickshaw_get_new(sender, instance, **kwargs):
    if instance.saved:
        Rickshaw(driver=instance.driver).save()


@receiver(pre_save, sender=Cargo)
def calculate_price(sender, instance, **kwargs):
    price = instance.product.unit_price * instance.quantity
    instance.price = price


@receiver(post_save, sender=Cargo)
def remove_stock_from_inventory(sender, instance, **kwargs):
    product = instance.product
    product.stock = product.stock - instance.quantity
    if not product.stock <= 0:
        product.save()
    else:
        raise RickshawCargoError("Product is out of stock or not enough stock to fulfill order")

# @receiver(post_save, sender=settings.RICKSHAW_USER_MODEL)
# def create_rickshaw(sender, instance, created, **kwargs):
#     if created:
#         Rickshaw(driver=instance).save()
