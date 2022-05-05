from django.db import models
from django.contrib.auth.models import User
from goodies.models import Product


class Sale(models.Model):
    serverby = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer = models.CharField(max_length=100)
    buyercontact = models.IntegerField()
    clientemail = models.EmailField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.serverby)


class Order(models.Model):
    buyer = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dateordered = models.DateTimeField(auto_now_add=True, auto_now=False)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.buyer
