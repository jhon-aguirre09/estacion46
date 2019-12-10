from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

class Inventory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.CharField(max_length=80)
    # codigo = models.ForeignKey(Product, related_name='existings', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=80)
    cantidad = models.IntegerField()
    fecha_Ingreso = models.DateField(auto_now=True)

    def __str__(self):
        return self.producto

    def get_absolute_url(self):
        return reverse('inventory:all')
