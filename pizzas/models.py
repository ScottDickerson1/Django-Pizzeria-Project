from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pizza_name

    class Meta: 
        verbose_name_plural = 'Pizza'

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topping_name

    class Meta:
        verbose_name_plural = 'Topping'