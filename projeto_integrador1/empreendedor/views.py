from django.shortcuts import render

from .models import Empreendedor


def index(request):
    empreendedores_list = Empreendedor.objects.order_by('nome')[:5]
    context = {'empreendedores_list': empreendedores_list}
    return render(request, 'empreendedor/index.html', context)
