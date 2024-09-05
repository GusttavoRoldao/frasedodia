from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('atualizar_texto', views.atualiza_texto, name='atualizar_texto'),
]