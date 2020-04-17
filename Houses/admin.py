from django.contrib import admin
from .models import Properties, Subscription, SubBreakDown

# Register your models here.
admin.site.register(Properties)
admin.site.register(Subscription)
admin.site.register(SubBreakDown)
