from django.shortcuts import render
# from .models import Usuario

# Create your views here.

app_name='usuarios'

def login(request):
	return render(request, 'usuarios/login.html')