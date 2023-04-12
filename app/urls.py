from django.urls import path
from app import views

#se utiliza para especificar la url app:..., en base.html
app_name = 'app'

urlpatterns = [
    path('', views.mi_vista, name='app'),
    path('crear-juego/', views.crear_juego, name='alta_juego'),
    path('juegos/', views.lista_juegos, name='consultar_juegos'),
    
]