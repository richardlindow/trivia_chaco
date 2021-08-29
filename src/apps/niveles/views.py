from django.shortcuts import render
from .models import Nivel
from django.views.generic import ListView

# Create your views here.

class NivelListView(ListView):
	model = Nivel
	template_name = 'niveles/niveles.html' # Esto lo tengo que redirigir a 'usuario/home.html' ???
	context_object_name = 'niveles' # define al objeto como niveles en vez de object_list en el template

def jugar_view(request, pk):
	nivel = Nivel.objects.get(pk=pk)
	return render(request, 'niveles/jugar.html', {'obj': nivel})
