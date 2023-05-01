from django.db import models
#from ckeditor.fields import RichTextField

# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    desarrollo = models.CharField(max_length=50)
    dispositivo = models.CharField(max_length=50)
    genero = models.CharField(max_length=100)
    #descripcion = RichTextField()
    
    
    def __str__(self):
        campo_desc= f'nombre:{self.nombre} - desarrollo:{self.desarrollo} - dispositivo:{self.dispositivo} - genero:{self.genero}'
        return campo_desc
        
    