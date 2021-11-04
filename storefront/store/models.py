from django.db import models
from django.db.models.deletion import PROTECT


class Collection(models.Model):
    title= models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    description= models.TextField
    budget= models.DecimalField(max_digits=8,decimal_places=2)
    last_update= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)
    quantity= models.IntegerField()
    collection= models.ForeignKey(Collection, on_delete=PROTECT) # The product won't be deleted even if we accidentally delete a collection

class Customer(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.EmailField(unique=True)
    phone= models.CharField(max_length=255)
    bought= models.IntegerField()
    sold= models.IntegerField()

class Order(models.Model):
    
    PAYMENT_STATUS_PENDING= 'P'
    PAYMENT_STATUS_RECEIVED= 'R'
    PAYMENT_STATUS_HANDED_OVER= 'H'
    PAYMENT_STATUS_CHOICES= [
        (PAYMENT_STATUS_RECEIVED, 'Pending'),
        (PAYMENT_STATUS_RECEIVED, 'Recieved'),
        (PAYMENT_STATUS_HANDED_OVER, 'Handed Over')
    ]

    placed_at= models.DateTimeField(auto_now_add=True)
    payment_stats= models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer= models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.PROTECT)
    product= models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity= models.PositiveSmallIntegerField()
    unit_price= models.DecimalField(max_digits=8,decimal_places=2)

class Address(models.Model):
    street= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    # If the customer is deleted, the address is deleted as well (Cascade)
    # This is a one-to-many relationship. Different customers can have the same address
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE) 

class Cart(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveSmallIntegerField()