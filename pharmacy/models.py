from django.db import models

# Create your models here.


class Pharmacy(models.Model):
    name = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=20)
    cuit = models.IntegerField()
    email = models.EmailField()
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    nro_registro = models.IntegerField()
    password = models.IntegerField()

    def get_location(self):
        return {
            'city': self.city,
            'province': self.province,
            'country': self.country
        }

