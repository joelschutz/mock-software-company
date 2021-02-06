from datetime import date

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from sales.models import License

@receiver(pre_save, sender=License)
def set_activation_date(sender, instance, **kwargs):
    try:
        active_before = sender.objects.get(id=instance.id).activated
    except ObjectDoesNotExist:
        return
    active_after = instance.activated
    if (not active_before) and active_after:
        instance.activation_date = date.today()
    if active_before and (not active_after):
        instance.activation_date = None