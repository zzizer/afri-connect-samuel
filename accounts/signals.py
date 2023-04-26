from .models import NewUser
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=NewUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our AfriConnect Uganda Ltd!'
        message = 'Dear {},\n\nAfriConnect is a Private company located in Uganda, It basically offers employment opportunity services within the country and across the globe\n\nThank you for signing up for our App and we are glad that you finally found us!'.format(instance.user_name)
        from_email = 'africonnectugltd301@gmail.com'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
