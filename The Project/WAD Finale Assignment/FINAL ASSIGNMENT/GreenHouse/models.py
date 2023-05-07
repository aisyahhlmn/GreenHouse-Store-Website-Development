from django.db import models

# Create your models here.

class SignIn(models.Model):
    Name = models.TextField(max_length=100)
    Birth_Date = models.DateField(null=True)
    Email_Id = models.CharField(max_length=100, primary_key=True)
    Mobile_Number = models.CharField(max_length=20)
    Gender = models.TextField(max_length=10)
    Address = models.CharField(max_length=100)
    City = models.TextField(max_length=20, null=True)
    Pin_Code = models.IntegerField()
    State = models.TextField(max_length=20)
    Country = models.TextField(max_length=20)
    password = models.CharField(max_length=50, null=True)
    retype_password = models.CharField(max_length=50, null=True)

class SignUp(models.Model):
    Email_Id = models.ForeignKey(SignIn, on_delete=models.CASCADE)


class Checkout(models.Model):
    custemail = models.ForeignKey(SignIn, on_delete=models.CASCADE)
    custname = models.TextField(max_length=100)
    custphone = models.CharField(max_length=11)
    custstate = models.TextField(max_length=20)
    custaddress = models.CharField(max_length=100)
    custZIP = models.IntegerField()
    date = models.DateField()

class Product(models.Model):
    prodid = models.CharField(max_length=20, primary_key=True)
    prodname = models.TextField(max_length=60)
    prodprice = models.IntegerField()
    prodcategory = models.TextField(max_length=100)

class Cart(models.Model):
    prodid = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()