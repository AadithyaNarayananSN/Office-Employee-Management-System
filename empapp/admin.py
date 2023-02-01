from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(employee)

admin.site.register(department)

admin.site.register(Role)