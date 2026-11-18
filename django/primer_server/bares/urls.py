from django.urls import path
from bares import views


urlpatterns = [
    path("", views.portada, name="portada"),
    path("bares/", views.listado, name="listado"),
]