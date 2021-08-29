from django.shortcuts import render

# Create your views here.

app_name='preguntas'

def crear_pregunta(request):
	return render(request, 'preguntas/crear-preg.html')