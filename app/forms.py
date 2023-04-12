from django import forms

class CreacionJuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    desarrollo = forms.CharField(max_length=20)
    dispositivo = forms.CharField(max_length=20)
    genero = forms.CharField(max_length=50)
       
class BuscarJuego(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    desarrollo = forms.CharField(max_length=20, required=False)