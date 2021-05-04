from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #text = models.TextField()
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.name