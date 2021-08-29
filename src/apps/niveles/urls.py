from django.urls import path
from .views import NivelListView, jugar_view

app_name = 'niveles'

urlpatterns = [
	path('', NivelListView.as_view(), name = 'listar-niveles'),
	path('<pk>/', jugar_view, name = 'jugar-niveles'),
]