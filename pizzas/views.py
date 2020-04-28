from django.shortcuts import render
from .models import Topping 

from .models import Pizza, Topping

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizza_list(request):
   
    pizza_list = Pizza.objects.order_by('date_added')

    context = {'pizza_list':pizza_list}

    return render(request, 'pizzas/pizza_list.html', context)

def pizza(request, pizza_id):

    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html',context)