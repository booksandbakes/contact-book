from django.contrib import admin

# Register your models here.
from .models import user,contacts

admin.site.register(user)
admin.site.register(contacts)
