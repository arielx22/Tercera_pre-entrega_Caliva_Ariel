from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from users.models import InformacionExtra
from users.forms import FormularioCreacion, EdicionDatosUsuario



# Create your views here.
def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            InformacionExtra.objects.get_or_create(user=request.user)
            return redirect('app:app')
        else:
            return render(request, 'login.html', {'formulario': formulario})
            
    
    formulario = AuthenticationForm()
    return render(request, 'login.html', {'formulario': formulario})
def registro(request):
    
    if request.method == "POST":
        formulario = FormularioCreacion(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('users:login')
        else:
            return render(request, 'registro.html', {'formulario': formulario})
            

    formulario = FormularioCreacion()
    return render(request, 'registro.html', {'formulario': formulario})


@login_required
def editar_perfil(request):
    if request.method == "POST":
        formulario = EdicionDatosUsuario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                request.user.informacionextra.avatar = formulario.cleaned_data.get('avatar')
            request.user.informacionextra.save()
            formulario.save()
            return redirect('app:app')
        else:
            return render(request, 'editar_perfil.html', {'formulario': formulario})
            
    formulario = EdicionDatosUsuario(initial={'avatar': request.user.informacionextra.avatar}, instance=request.user)
    return render(request, 'editar_perfil.html', {'formulario': formulario})

class CambioContrasenia(PasswordChangeView):
    template_name = 'cambiar_contrasenia.html'
    success_url = reverse_lazy('users:editar_perfil')
       
    




