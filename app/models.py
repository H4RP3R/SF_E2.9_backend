import uuid
import os
import time
import smtplib

from django.db import models
from django.core.mail import send_mail


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=255)
    address = models.EmailField(max_length=255)
    text = models.TextField()
    delay = models.PositiveIntegerField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.address}'

    def send(self):
        if not self.sent:
            time.sleep(self.delay)
            send_mail(
                self.subject,
                self.text,
                from_email=None,
                recipient_list=[self.address, ],
                fail_silently=False,
            )
            print('SENT', self)
