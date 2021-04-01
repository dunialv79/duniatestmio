from django.contrib import admin
from .models import almacen
# Register your models here.

class almacenadmin(admin.ModelAdmin):
     readonly_fields=('creacion','actualizacion')

admin.site.register(almacen, almacenadmin)
