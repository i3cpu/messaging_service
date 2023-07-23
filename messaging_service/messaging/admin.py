from django.contrib import admin

from messaging.models import Campaign, Message, Client


admin.site.register(Client)
admin.site.register(Campaign)
admin.site.register(Message)
