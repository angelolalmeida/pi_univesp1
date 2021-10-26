from django.contrib import admin
from .models import Categoria, Empreendedor, Lancamento

# Register your models here.
class EmpreendedorAdmin(admin.ModelAdmin):
  list_display = ('id','nome')
  
class CategoriaAdmin(admin.ModelAdmin):
  list_display = ('id','nome')  
  
class LancamentoAdmin(admin.ModelAdmin):
  list_display = ('id','empreendedor', 'nome_fornecedor','data_vencimento', 'categoria')  


admin.site.register(Empreendedor, EmpreendedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Lancamento, LancamentoAdmin)