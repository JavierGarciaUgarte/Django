from django.urls import path
from .import views

app_name='principal'

urlpatterns = [
    path("",views.holaDjango,name="holaDjango"),
    path('pepe', views.pepe, name='holapepe'),
    path('indice', views.indice, name='indice'),
    path('<str:nombre>', views.holatu, name='holatu' ),
    
    ]