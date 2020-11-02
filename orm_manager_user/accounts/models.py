from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    name=models.CharField( max_length=250,null=True)
    phone=models.CharField( max_length=250,null=True)
    email=models.CharField( max_length=250,null=True)



# =========================================================change
class Customer(models.Model):
    name=models.CharField( max_length=250,null=True)
    phone=models.CharField( max_length=250,null=True)
    email=models.CharField( max_length=250,null=True)
    date_created = models.DateTimeField( auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField( max_length=250,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Books','Books'),
        ('Videos','Videos'),
        ('Music','Music')
    )
    name=models.CharField( max_length=250,null=True)
    price=models.IntegerField(null=True)
    category=models.CharField( max_length=250,null=True,choices=CATEGORY)
    description=models.CharField( max_length=250,null=True,blank=True)
    date_created= models.DateTimeField( auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    

class Permission(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Allowed','Allowed'),
        ('Denied','Denied')
    )
    customer=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_created= models.DateTimeField( auto_now_add=True,null=True)
    status=models.CharField(max_length=250,null=True,choices=STATUS)


    def __str__(self):
        return self.product.name