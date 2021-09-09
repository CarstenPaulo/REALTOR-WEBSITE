from typing import Text
from django import forms
from django.forms import widgets
from django.forms.fields import CharField
from django.forms.widgets import NumberInput, TextInput, Textarea


class contatoemail(forms.Form):
    nome = forms.CharField(widget=TextInput(attrs={'placeholder':'Nome'}))
    sobrenome = forms.CharField(widget=TextInput(attrs={'placeholder':'Sobrenome'}))
    telefone = CharField(widget=NumberInput(
        attrs={'placeholder': '(DDD) 9 9999-9999'}))
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': 'Email'}))
    assunto = forms.CharField(widget=Textarea(attrs={'placeholder': 'Assunto'}))
   



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].required = True
        self.fields['sobrenome'].required = True
        self.fields['telefone'].required = True
        self.fields['email'].required = True
        self.fields['assunto'].required = True
