from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.listar, name='listar'),
    path('<int:listagem_id>', views.listagem, name='listagem'),
    path('pesquisar', views.pesquisar, name='pesquisar'),
]
