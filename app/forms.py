from django import forms

class CreacionJuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    desarrollo = forms.CharField(max_length=50)
    dispositivo = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=100)
       
class BuscarJuego(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    desarrollo = forms.CharField(max_length=50, required=False)