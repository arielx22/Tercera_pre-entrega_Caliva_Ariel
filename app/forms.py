from django import forms

class BaseJuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    desarrollo = forms.CharField(max_length=50)
    dispositivo = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=100)

class CreacionJuegoFormulario(BaseJuegoFormulario):
    ...
    
class ModificarJuegoFormulario(BaseJuegoFormulario):
    ...
       
class BuscarJuego(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    desarrollo = forms.CharField(max_length=50, required=False)

