from django import forms
     
class BuscarJuego(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    desarrollo = forms.CharField(max_length=50, required=False)

