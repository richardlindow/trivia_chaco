from django.db import models

# Create your models here.

NIVEL_DIF = (
	('Fácil', 'Fácil'),
	('Medio', 'Medio'),
	('Dicífil', 'Difícil'),
	('Chaqueñaso', 'Chaqueñaso'),
	)

class Nivel(models.Model):
	nombre = models.CharField(max_length=120)
	descripcion = models.CharField(max_length=250)
	cantidad_de_preguntas =  models.IntegerField()
	puntaje_minimo_para_aprobar = models.IntegerField()
	dificultad = models.CharField(max_length=10, choices=NIVEL_DIF)

	def __str__(self):
		return f"{self.nombre} - {self.descripcion}"

	def get_preguntas(self): # con listas lo puedo reordenar
		return self.pregunta_set.all()[:self.cantidad_de_preguntas] #limitar la cantidad de preguntas que trae la función

	class Meta:
		verbose_name_plural = 'Niveles'