from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Empreendedor
from .models import Categoria


# @login_required()
def index(request):    
    empreendedores_list = Empreendedor.objects.order_by('nome')[:5]
    context = {'empreendedores_list': empreendedores_list}
    return render(request, 'empreendedor/index.html', context)
  
def categorias(request):
  categorias_list = Categoria.objects.order_by('nome')
  context = {'categorias_list': categorias_list}
  return render(request, 'empreendedor/categorias_list.html', context)


def detalhe_empreendedor(request, id_empreendedor):
    #empreendedor = Empreendedor.objects.get(id=id_empreendedor)
    empreendedor = get_object_or_404(Empreendedor, id=id_empreendedor)
    context = {'empreendedor': empreendedor}
    return render(request, 'empreendedor/detalhe_empreendedor.html', context)

def detalhe_categoria(request, id_categoria):
  categoria = get_object_or_404(Categoria, id=id_categoria)
  context = {'categoria': categoria}
  return render(request, 'empreendedor/categoria_detalhes.html', context)
