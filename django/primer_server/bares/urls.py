from django.urls import path
from bares import views


urlpatterns = [
    path("", views.portada, name="portada"),
    path("bares/<int:pk>/", views.detalle, name="detalle"),
    path("inspector/", views.inspector, name="inspector"),
    path("bares/buscar/", views.buscar, name="buscar")
]