from django.db import models

# Create your models here.

class Fantuan(models.Model):
    id=models.IntegerField(primary_key=True)
    shop=models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    address = models.CharField(max_length=200)
    phone=models.CharField(max_length=50)
    food=models.CharField(max_length=200)
    time=models.CharField(max_length=50)
    rate=models.IntegerField()

class Fantuan2(models.Model):
    id=models.IntegerField(primary_key=True)
    photo1=models.CharField(max_length=500)
    desh1=models.CharField(max_length=50)
    price1=models.IntegerField()
    photo2 = models.CharField(max_length=500)
    desh2 = models.CharField(max_length=50)
    price2 = models.IntegerField()
    photo3 = models.CharField(max_length=500)
    desh3 = models.CharField(max_length=50)
    price3 = models.IntegerField()
    photo4 = models.CharField(max_length=500)
    desh4 = models.CharField(max_length=50)
    price4 = models.IntegerField()

class user(models.Model):
    num=models.BigIntegerField(primary_key=True)
    nickname=models.CharField(max_length=16)
    password=models.CharField(max_length=16)

class Cart(models.Model):
    photo=models.CharField(max_length=500)
    desh=models.CharField(max_length=50)
    number=models.IntegerField()
    price=models.IntegerField()
