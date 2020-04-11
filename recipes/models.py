from django.db import models
from patient.models import MedicalPatient
from medicine.models import Medicine

# Create your models here.


class Recipe(models.Model):
    STATUS_CHOICES = (
        ('rechazado', 'Rechazado'),
        ('aprobado', 'Aprobado'),
        ('pendiente', 'Pendiente'),
        ('entregado', 'Entregado'),
        ('en camino', 'En camino')
    )

    date = models.DateTimeField(unique=True, auto_now_add=True)

    patient = models.ForeignKey(MedicalPatient, related_name='patient', on_delete=models.CASCADE, unique=True)
    medicine = models.ForeignKey(Medicine, related_name='medicine', on_delete=models.CASCADE)

