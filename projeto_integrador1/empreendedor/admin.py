from django.contrib import admin
from .models import Empreendedor

# Register your models here.
class EmpreendedorAdmin(admin.ModelAdmin):
  list_display = ('id','nome')


admin.site.register(Empreendedor, EmpreendedorAdmin)