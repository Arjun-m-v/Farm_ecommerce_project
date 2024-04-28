from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class products(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    image=models.ImageField(upload_to="product_images")
    options=(
        ('kg','kg'),
        ('litre','litre'),
        ('packet','packet'),
        ('bottle','bottle'),
        ('tin','tin'),
        ('dozen','dozen'),
        ('cownumber','cownumber'),
        ('goatnumber','goatnumber'),
        ('chickennumber','chickennumber'),
        ('pignumber','pignumber'),
        ('ducknumber','ducknumber'),
        ('rabbitnumber','rabbitnumber'),
        ('horsenumber','horsenumber'),
    )
    categories=models.CharField(max_length=200,choices=options)
    stock=models.IntegerField()
    def __str__(self):
        return self.title
    

class Cart(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)

class Orders(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=500)
    options=(
        ('Order Placed','Order Placed'),
        ('Cancelled','Cancelled'),
        ('Shipped','Shipped'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered')
    )
    order_status=models.CharField(max_length=100,choices=options)



class Review(models.Model):
    review=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)