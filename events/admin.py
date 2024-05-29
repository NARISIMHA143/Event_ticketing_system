from django.contrib import admin

# Register your models here.
from events.models import Events,EventType

admin.site.register(Events)
admin.site.register(EventType)