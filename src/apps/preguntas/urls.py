from django.urls import path
from . import views

app_name = 'preguntas'

urlpatterns = [
	path('', views.crear_pregunta,  name='crear-preg')
]
