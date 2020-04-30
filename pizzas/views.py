from django.shortcuts import render, redirect
from .forms import addPizza, addComment
from .models import Pizza

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

def new_pizza(request):
    if request.method != 'POST':
        form = addPizza()
    else:
        form = addPizza(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza_list')

    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html', context)


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = addComment()
    else:
        form = addComment(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza': pizza}
    return render(request, 'pizzas/new_comment.html', context)