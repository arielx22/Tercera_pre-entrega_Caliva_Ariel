from django.shortcuts import render, redirect
from app.models import Juego
from app.forms import BuscarJuego

#CBV
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
def mi_vista(request):
    return render(request, 'index.html')

def nuestra_vista(request):
    return render(request, 'nosotros.html')


def lista_juegos(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    desarollo_a_buscar = request.GET.get('desarrollo', None)
    
    if nombre_a_buscar or desarollo_a_buscar:
        juegos = Juego.objects.filter(nombre__icontains=nombre_a_buscar,
                                      desarrollo__icontains=desarollo_a_buscar)
    else:
        juegos = Juego.objects.all()
    
    formulario_busqueda = BuscarJuego()
    return render(request, 'consultar_juegos.html', {'juegos': juegos, 
                                                     'formulario': formulario_busqueda})
    

# vistas CBV (clases basada en vistas)
#class ListaJuegos(ListView):
#    model = Juego
#    template_name = 'CBV/consultar_juegos.html'
    
class CrearJuego(CreateView):
    model = Juego
    template_name = 'CBV/alta_juego.html'
    success_url = reverse_lazy('app:consultar_juegos')
    fields = ['nombre', 'desarrollo','dispositivo','genero','descripcion','imagen']
    
class ModificarJuego(LoginRequiredMixin, UpdateView):
    model = Juego
    template_name = 'CBV/modificar_juego.html'
    success_url = reverse_lazy('app:consultar_juegos')
    fields = ['nombre', 'desarrollo','dispositivo','genero','descripcion','imagen']
    
class EliminarJuego(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = 'CBV/eliminar_juego.html'
    success_url = reverse_lazy('app:consultar_juegos')
    
class MostrarJuego(DetailView):
    model = Juego
    template_name = 'CBV/mostrar_juego.html'



