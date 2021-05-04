from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=60)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')


    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #text = models.TextField()
    name = models.CharField(max_length=60)

    #class Meta:
        #verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."
