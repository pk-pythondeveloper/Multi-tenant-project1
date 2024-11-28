from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True)  # Domain or identifier

    def __str__(self):
        return self.name

class Product(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)  # Tenant association
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
