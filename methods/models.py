from django.db import models

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    year_production = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=25)


# Связь один ко многим
class Customer(models.Model):                   # Клиенты
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=55)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

