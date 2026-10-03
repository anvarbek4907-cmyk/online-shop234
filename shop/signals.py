from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cart, Customer


@receiver(post_save, sender=User)
def create_customer_and_cart(sender, instance, created, **kwargs):
    """Yangi User yaratilganda unga Customer va Cart avtomatik yaratiladi."""
    if created:
        customer = Customer.objects.create(user=instance)
        Cart.objects.create(customer=customer)
