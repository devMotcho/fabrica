from .models import Inventary, Product, Production
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver


@receiver(post_save, sender=Product)
def create_inventary(sender, instance, created, **kwargs):
    if created:
        Inventary.objects.create(product=instance, total_quantity=0)



@receiver(m2m_changed, sender=Inventary.productions.through)
def calculate_total_stock(sender, instance, action, **kwargs):
    total_quantity = sum(item.quantity for item in instance.productions.all())
    instance.total_quantity = total_quantity
    instance.save()

@receiver(post_save, sender=Production)
def update_inventary(sender, instance, created, **kwargs):
    if created:
        inventary = Inventary.objects.get(product=instance.product)
        inventary.productions.add(instance)