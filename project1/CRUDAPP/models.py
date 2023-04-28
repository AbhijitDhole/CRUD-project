from django.db import models

# Create your models here.
class Order(models.Model):
    o_id = models.IntegerField()
    o_name = models.CharField(max_length=50)
    o_price = models.FloatField()
    o_date = models.DateField()
    product = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    add = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.id}---{self.o_name}---{self.add}"