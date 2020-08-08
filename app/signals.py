import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import Email


@receiver(post_save, sender=Email)
def send_email(sender, instance, **kwargs):
    t = threading.Thread(target=instance.send)
    t.start()
    t.join()
