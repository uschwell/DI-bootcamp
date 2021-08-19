from django.db import models



class Family(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=40,default='dane_joe')



class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    legs = models.IntegerField(default=4)
    weight = models.IntegerField(default=100)
    height = models.IntegerField(default=100)
    speed = models.IntegerField(default=10)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)



def __str__(self):
    return self.title



