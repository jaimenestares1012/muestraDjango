from django.contrib import admin

# Register your models here.
from .models import Servicio

class servicioadmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
admin.site.register(Servicio, servicioadmin)


