from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categorias', views.categorias, name='categorias_list'),
    path('<int:id_empreendedor>', views.detalhe_empreendedor, name='detalhe_empreendedor'),    
]