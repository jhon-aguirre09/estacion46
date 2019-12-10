from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    codigo = models.CharField(max_length=80)
    codigo_Interno = models.CharField(max_length=80)
    presentacion = models.CharField(max_length=80)
    precio_Ingreso= models.FloatField()
    precio_Venta = models.FloatField()
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('products:all')

    class Meta:
        unique_together = ['nombre','codigo_Interno']
