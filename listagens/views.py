from typing import List
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from listagens.choices import escolhas_precos, escolhas_cidades,escolhas_imoveis


from .models import Listagen

# Create your views here.
def listar(request): 
    listagens = Listagen.objects.order_by('-data_listada').filter(publicado=True)

    paginator = Paginator(listagens, 6) #quantitade de listagens por páginas
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listagens':paged_listings
    }

    return render(request, 'listagens/listar.html', context)

def listagem(request, listagem_id):
    listagem = get_object_or_404(Listagen, pk=listagem_id)
    context = {
        'listagem':listagem,
    }
    return render(request, 'listagens/listagens.html', context)

def pesquisar(request):
    queryset_list = Listagen.objects.all().filter(publicado=True)

    # palavraschaves
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                descricao__icontains=keywords)


       # cidade
    if 'cidade' in request.GET:
        cidade = request.GET['cidade']
        if cidade:
            queryset_list = queryset_list.filter(cidade__iexact=cidade)

    
     # tipoimovel
    if 'tipo_de_imovel' in request.GET:
        tipo_de_imovel = request.GET['tipo_de_imovel']
        if tipo_de_imovel:
            queryset_list = queryset_list.filter(tipo_de_imovel__iexact=tipo_de_imovel)

    
     # preco
    if 'preco' in request.GET:
        preco = request.GET['preco']
        if preco:
            queryset_list = queryset_list.filter(preco__lte=preco)


    context = {
        'escolhas_precos':escolhas_precos,
        'escolhas_cidades':escolhas_cidades,
        'escolhas_imoveis':escolhas_imoveis,
        'listagens': queryset_list
    }
    return render(request, 'listagens/pesquisar.html', context)
    