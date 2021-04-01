from django.db import models

# Create your models here.

class almacen (models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    img=models.ImageField(upload_to='fronend')
    creacion=models.DateTimeField(auto_now_add=True)
    actualizacion=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='almacen'
        verbose_name_plural='almacenes'
    def __str__(self):
        return self.nombre
