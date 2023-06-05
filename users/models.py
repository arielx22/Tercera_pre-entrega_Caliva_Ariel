from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 

# Create your models here.

class InformacionExtra(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = RichTextField(blank=True)
    
    def __str__(self):
        return self.user.username
    

    
    
    
