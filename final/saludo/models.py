from django.db import models

class Categoria(models.Model):
	nombre= models.CharField(max_length=100)

class Gasto(models.Model):
	descripcion= models.TextField(max_length=100)
	fecha= models.DateField(auto_now=True)
	monto= models.DecimalField(max_digits=3, decimal_places=1)
	categoria=models.ForeignKey(Categoria,  on_delete=models.CASCADE)

	def __str__(self):
		return self.descripcion
