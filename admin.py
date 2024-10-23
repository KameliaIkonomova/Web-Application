from django.contrib import admin

from .models import Poll, Option, Announcement

# registering in the admin panel our models
admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Announcement)
