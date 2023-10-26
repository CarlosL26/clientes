from django import forms
from django.forms import EmailInput
from .models import Clientes , Contacto
class FormClientes(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = "__all__"
        

class ContactoForm(forms.ModelForm):
    class Meta :
        model=Contacto
        fields="__all__"
        widgets = {
            'email':EmailInput(attrs={'type':'email'}),
            }