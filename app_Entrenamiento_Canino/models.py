from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    fecha_registro = models.DateField()
    fecha_nacimiento = models.DateField()
    comentarios = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: PERRO
# ==========================================
class Perro(models.Model):
    id_perro = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='perros')
    # Relación 1 a muchos: un cliente puede tener varios perros

    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    color = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"