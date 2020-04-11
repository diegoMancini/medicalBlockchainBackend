from django.db import models

# Create your models here.


class Doctor(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)
    dni = models.IntegerField()
    nro_matricula_nacional = models.IntegerField()
    nro_matricula_provincial = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def get_location(self):
        return {
            'city': self.city,
            'province': self.province,
            'country': self.country
        }

    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"