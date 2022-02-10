from django import forms

class FormularioArquitectura(forms.form):
    region = forms.CharField(max_length=40)
    num_lista = forms.IntegerField()
    num_sku= forms.IntegerField()
    