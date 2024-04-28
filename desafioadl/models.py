from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return f'Tarea [{self.id}] {self.descripcion}'

class SubTarea(models.Model):
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return f'Subtarea [{self.id}] {self.descripcion}'