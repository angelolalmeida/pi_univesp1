from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Empreendedor


# @login_required()
def index(request):    
    empreendedores_list = Empreendedor.objects.order_by('nome')[:5]
    context = {'empreendedores_list': empreendedores_list}
    return render(request, 'empreendedor/index.html', context)


def detalhe_empreendedor(request, id_empreendedor):
    #empreendedor = Empreendedor.objects.get(id=id_empreendedor)
    empreendedor = get_object_or_404(Empreendedor, id=id_empreendedor)
    context = {'empreendedor': empreendedor}
    return render(request, 'empreendedor/detalhe_empreendedor.html', context)
