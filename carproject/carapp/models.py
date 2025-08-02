from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    class Meta:
        db_table="contact"

class apponment(models.Model):
    vehicle_year=models.CharField(max_length=100)
    vehicle_make=models.CharField(max_length=100)
    vehicle_mileage=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    service=models.CharField(max_length=100)
    Name2=models.CharField(max_length=100)
    email2=models.CharField(max_length=100)
    number2=models.CharField(max_length=100)
    message2=models.CharField(max_length=100)
    class Meta:
        db_table="apponment"
