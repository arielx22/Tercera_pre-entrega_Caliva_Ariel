from django.shortcuts import render, redirect
from app.models import Juego
from app.forms import CreacionJuegoFormulario, BuscarJuego

# Create your views here.
def mi_vista(request):
    return render(request, 'index.html')
    
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