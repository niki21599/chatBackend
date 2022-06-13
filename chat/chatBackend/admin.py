from django.contrib import admin
from chatBackend.models import Chat
from chatBackend.models import Message
# Register your models here.

admin.site.register(Message)
admin.site.register(Chat)