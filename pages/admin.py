from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)