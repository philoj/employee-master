from django.contrib import admin

# Register your models here.
from apps.employees.models import User

admin.site.register(User)