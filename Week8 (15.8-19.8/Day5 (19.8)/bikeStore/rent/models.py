from django.db import models
from django import forms
from django.forms import ModelForm

class Address(models.Model):
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    postal_code = models.IntegerField()

    def __str__(self):
        return f'{self.address}, {self.city}, {self.country}, {self.postal_code}'



class Customer(models.Model):
    first_name = models.CharField(max_length=20) 
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=25)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)



class Vehicle_Type(models.Model):
	name = models.CharField(max_length=200)


class Vehicle_Size(models.Model):
    name = models.CharField(max_length=200)

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    date_created =  models.DateTimeField()
    real_cost = models.IntegerField()
    size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

    def is_rented(self):
        rentals = self.rental_set.filter(return_date__isnull=True)
        if len(rentals) > 0:
            return True
        return False

class Rental(models.Model):
	rental_date = models.DateTimeField()
	return_date = models.DateTimeField(null=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)






