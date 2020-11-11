from django.contrib import admin

from .models import Guest_User, Posts

admin.site.register(Guest_User)
admin.site.register(Posts)