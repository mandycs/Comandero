from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nombre

class Comanda(models.Model):
    habitacion = models.PositiveIntegerField()
    mesa = models.PositiveSmallIntegerField()
    platos = models.ManyToManyField(Plato, through='DetalleComanda')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comanda en Habitación {self.habitacion}, Mesa {self.mesa}"

    def calcular_precio_total(self):
        # Calcular el precio total sumando los precios de los platos de la comanda
        precio_total = sum(detalle.cantidad * detalle.plato.precio for detalle in self.detallecomanda_set.all())
        return precio_total

class DetalleComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.cantidad}x {self.plato.nombre} en Comanda {self.comanda.id}"

class HistorialComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comanda {self.comanda.id} - {self.fecha}"