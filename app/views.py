from django.shortcuts import render, redirect
from app.models import Juego
from app.forms import CreacionJuegoFormulario, BuscarJuego, ModificarJuegoFormulario

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

    
def crear_juego(request):
    
    if request.method == "POST":
        formulario = CreacionJuegoFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            juego = Juego(nombre=datos_correctos['nombre'], desarrollo=datos_correctos['desarrollo']
                          , dispositivo=datos_correctos['dispositivo'], genero=datos_correctos['genero'])
            juego.save()

            return redirect('app:consultar_juegos')
            
    
    formulario = CreacionJuegoFormulario()
    return render(request, 'alta_juego.html', {'formulario': formulario})

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
    
def eliminar_juego(request, id_juego):
    juego_a_eliminar = Juego.objects.get(id=id_juego)
    juego_a_eliminar.delete()
    return redirect('app:consultar_juegos')

def modificar_juego(request, id_juego):
    juego_update = Juego.objects.get(id=id_juego)
    
    if request.method == "POST":
        formulario = ModificarJuegoFormulario(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            
            juego_update.nombre = data_limpia['nombre']
            juego_update.desarrollo = data_limpia['desarrollo']
            juego_update.dispositivo = data_limpia['dispositivo']
            juego_update.genero = data_limpia['genero']
            
            juego_update.save()
            
            return redirect('app:consultar_juegos')
        else:
            return render(request, 'modificar_juego.html', {'formulario': formulario, 'id_juego': id_juego})
    
    formulario = ModificarJuegoFormulario(initial={'nombre': juego_update.nombre, 'desarrollo': juego_update.desarrollo,
                                                   'dispositivo': juego_update.dispositivo,'genero': juego_update.genero})
    return render(request, 'modificar_juego.html', {'formulario': formulario, 'id_juego': id_juego})

def mostrar_juego(request, id_juego):
    juego_mostrar = Juego.objects.get(id=id_juego)
    return render(request, 'mostrar_juego.html', {'juego_mostrar': juego_mostrar})

# vistas CBV (clases basada en vistas)
class ListaJuegos(ListView):
    model = Juego
    template_name = 'CBV/consultar_juegos.html'
    
class CrearJuego(CreateView):
    model = Juego
    template_name = 'CBV/alta_juego.html'
    success_url = reverse_lazy('app:consultar_juegos')
    fields = ['nombre', 'desarrollo','dispositivo','genero']
    
class ModificarJuego(LoginRequiredMixin, UpdateView):
    model = Juego
    template_name = 'CBV/modificar_juego.html'
    success_url = reverse_lazy('app:consultar_juegos')
    fields = ['nombre', 'desarrollo','dispositivo','genero']
    
class EliminarJuego(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = 'CBV/eliminar_juego.html'
    success_url = reverse_lazy('app:consultar_juegos')
    
class MostrarJuego(DetailView):
    model = Juego
    template_name = 'CBV/mostrar_juego.html'



