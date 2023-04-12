from django.db import models

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=20)
    desarrollo = models.CharField(max_length=20)
    dispositivo = models.CharField(max_length=20)
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        campo_desc= f'nombre:{self.nombre} - desarrollo:{self.desarrollo} - dispositivo:{self.dispositivo} - genero:{self.genero}'
        return campo_desc
        
    