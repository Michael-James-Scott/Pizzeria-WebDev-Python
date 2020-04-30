from django.db import models

# Create your models here.
class Pizza(models.Model):
    text = models.CharField(max_length=30)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    top_choices = (
        ('B', 'Bacon'),
        ('S', 'Sausage'),
        ('P', 'Pepperoni'),
        ('PN', 'Pineapple'),
        ('SP', 'Spinach'),
        ('M', 'Mushrooms'),
        ('C', 'Chicken'),
        ('A', 'Anchovies'),
        ('GP', 'Green Peppers'),
        ('RP', 'Red Peppers'),
    )
    #text = models.TextField()
    top_choice = models.CharField(max_length=2, choices=top_choices)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'
        
    

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
      
        verbose_name_plural = 'comments'
        
    def __str__(self):
        return f"{self.text[:50]}..."