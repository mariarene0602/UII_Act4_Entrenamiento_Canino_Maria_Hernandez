from django.contrib import admin
from .models import Cliente, Perro

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'email', 'telefono', 'fecha_registro')
    list_filter = ('fecha_registro',)
    search_fields = ('nombre', 'email', 'telefono')

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('id_perro', 'nombre', 'raza', 'color', 'peso', 'cliente')
    list_filter = ('raza', 'cliente')
    search_fields = ('nombre', 'raza', 'cliente__nombre')