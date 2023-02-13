from django.urls import path
from . import views

app_name = "ventas"

urlpatterns = [
    path("", views.index, name = "index"),
    path("registrar/", views.registrar, name = "registrar"),
    path("search/", views.search, name = "search"),
    path("search/person/", views.search_b, name = "searchperson"),
    path("enviar/", views.save, name="save")
]