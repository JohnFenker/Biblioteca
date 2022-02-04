from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'libros-2/', views.ListLibros2.as_view(), name="libros2"
    ),
    path(
        'libro-detalle/<pk>/', views.LibroDetailView.as_view(), name="libro-detalle"
    ),
    path(
        'libro-trg/', views.ListLibrosTrg.as_view(), name="libro-trg"
    )
]