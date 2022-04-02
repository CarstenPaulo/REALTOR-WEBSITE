from django.shortcuts import render
from listagens.models import Listagen
from corretor.models import Corretor
from django.core.mail import send_mail
from .forms import contatoemail
from django.contrib import messages
from listagens.choices import escolhas_precos, escolhas_cidades, escolhas_imoveis

# Create your views here.
def index(request):
    listagens = Listagen.objects.order_by('-data_listada').filter(publicado=True)[:6]
    context = {
            'listagens':listagens,
            'escolhas_precos':escolhas_precos,
            'escolhas_cidades':escolhas_cidades,
            'escolhas_imoveis':escolhas_imoveis,
        }
    return render(request,'index.html',context)

    
def sobre(request):
    corretores = Corretor.objects.all()
    context = {
        'corretores':corretores,
    }
    return render(request, 'sobre.html', context)


def faleconosco(request):
    if request.method =='GET':
        form=contatoemail()
    else: 
        form=contatoemail(request.POST)
        if form.is_valid():
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            telefone = request.POST.get('telefone')
            email = request.POST.get('email')
            assunto = request.POST.get('assunto')



        context = {
            'nome':nome,
            'sobrenome':sobrenome,
            'telefone':telefone,
            'email':email,
            'assunto':assunto,
        }

       
        dados = '''
        Nome: {}    

        Sobrenome: {}

        Telefone: {}

        Email: {}

        Assunto: {}

        
        '''.format(context['nome'],context['sobrenome'],context['telefone'],context['email'],context['assunto'])
        send_mail(context['nome'],dados, '', ['corvobrancoimobiliaria@gmail.com'])
        messages.success(request, 'Email enviado com sucesso,')
        form=contatoemail()
    return render(request, 'faleconosco.html',{'form':form})



def anuncieaqui(request):
    if request.method =='GET':
        form=contatoemail()
    else: 
        form=contatoemail(request.POST)
        if form.is_valid():
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            telefone = request.POST.get('telefone')
            email = request.POST.get('email')
            assunto = request.POST.get('assunto')



        context = {
            'nome':nome,
            'sobrenome':sobrenome,
            'telefone':telefone,
            'email':email,
            'assunto':assunto,
        }

       
        dados = '''
        Nome: {}    

        Sobrenome: {}

        Telefone: {}

        Email: {}

        Assunto: {}

        
        '''.format(context['nome'],context['sobrenome'],context['telefone'],context['email'],context['assunto'])
        send_mail(context['nome'],dados, '', ['corvobrancoimobiliaria@gmail.com'])
        messages.success(request, 'Email enviado com sucesso')
        form=contatoemail()
    return render(request, 'anuncieaqui.html',{'form':form})
