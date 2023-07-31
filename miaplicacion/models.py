from django.db import models


# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre}"
    
class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    redsocial= models.CharField(max_length=50)
    autorpublica = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Posteos(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    redsocial = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"