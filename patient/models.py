from django.db import models

# Create your models here.


class MedicalPatient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dni = models.IntegerField()
    medical_insurance = models.CharField(max_length=20)
    medical_insurance_plan = models.CharField(max_length=5)
    medical_insurance_member_number = models.CharField(max_length=12)
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def get_location(self):
        return {
            'city': self.city,
            'province': self.province,
            'country': self.country
        }

    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"