from django.contrib import admin
from .models import Clientes

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    
    list_display=('rubro','nombre','domicilio')
    list_filter=('vive','created')

admin.site.register(Clientes)
