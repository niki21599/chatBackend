from django.conf import settings
from django.db import models
from django.db.models.fields import DateTimeField

from django.utils import timezone

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class Chat(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_1")
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="user_2")
    now = timezone.now()
    
    created_at = DateTimeField(default=now)

class Message(models.Model):
    text = models.CharField(max_length=500)
    now = timezone.now()
    
    created_at = DateTimeField(default=now)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default=None, blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_message_set")
   

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created: 
        Token.objects.create(user=instance)