from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash

from users.models import InformacionExtra
from users.forms import FormularioCreacion, EdicionDatosUsuario, FormularioCambioContrasenia



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

def perfil(request):
    usuario = request.user
    return render(request, 'perfil.html', {'usuario': usuario})






@login_required
def editar_perfil(request):
    if request.method == "POST":
        formulario = EdicionDatosUsuario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            if 'avatar-clear' in request.POST:
                # Si se selecciona la opción de borrar el avatar
                request.user.informacionextra.avatar.delete()
            elif formulario.cleaned_data.get('avatar'):
                # Si se carga un nuevo avatar
                request.user.informacionextra.avatar = formulario.cleaned_data.get('avatar')            
            request.user.informacionextra.descripcion = formulario.cleaned_data.get('descripcion')
            request.user.informacionextra.save()
            formulario.save()
            return redirect('users:perfil')
        else:
            return render(request, 'editar_perfil.html', {'formulario': formulario})
            
    formulario = EdicionDatosUsuario(initial={'avatar': request.user.informacionextra.avatar, 'descripcion': request.user.informacionextra.descripcion}, instance=request.user)
    return render(request, 'editar_perfil.html', {'formulario': formulario})


@login_required
def cambiar_contrasenia(request):
    if request.method == "POST":
        formulario = FormularioCambioContrasenia(request.POST)
        
        if formulario.is_valid():
            contrasenia_nueva = formulario.cleaned_data.get('contrasenia_nueva')
            repetir_contrasenia = formulario.cleaned_data.get('repetir_contrasenia')
            
            if contrasenia_nueva == repetir_contrasenia:
                request.user.set_password(contrasenia_nueva)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('users:perfil')
        
        return render(request, 'cambiar_contrasenia.html', {'formulario': formulario})
    
    formulario = FormularioCambioContrasenia()
    return render(request, 'cambiar_contrasenia.html', {'formulario': formulario})





    
    
    


       
    




