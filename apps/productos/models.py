from django.db import models

# Create your models here.
class Product(models.Model):
    productTypes = [
        ('juguetes', 'Juguetes'),
        ('elect', 'Electronicos')
    ]
    name = models.CharField(max_length=30)
    productType = models.CharField(max_length=10, choices=productTypes)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL=True)
    date = models.DateField(auto_now=True)
    amount = models.IntegerField()
    def __str__(self):
        return self.date 