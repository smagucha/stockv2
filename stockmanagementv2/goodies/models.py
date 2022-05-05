from django.db import models


class Catergory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class QuantityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity__gte=1000)


class LessManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(quantity__lte=500)


class Product(models.Model):
    name = models.CharField(max_length=50)
    productcatergory = models.ForeignKey(Catergory, on_delete=models.CASCADE)
    weight = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = models.Manager()
    quantify = QuantityManager()
    lessquantity = LessManager()


    def __str__(self):
        return self.name


