# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to MovRek!'
        message = render_to_string('registration/welcome_email.txt', {'user': instance})
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email)
