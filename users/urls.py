from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

#se utiliza para especificar la url users:..., en base.html
app_name = 'users'

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    #path('perfil/<int:id_user>/', views.mostrar_perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambio-contrasenia/', views.CambioContrasenia.as_view(), name='cambio_contrasenia'),   
    
]