from django.db import models

# Create your models here.
class Pizza(models.Model):
    text = models.CharField(max_length=30)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # it allows us to set a special attribute telling Django to use 'Entries'
        # when it needs to refer to more than one entry. Without this, Django
        #would refer to multiple entries as 'Entrys'.
        verbose_name_plural = 'toppings'
        
    def __str__(self):
        return f"{self.text[:50]}..."