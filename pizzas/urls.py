from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    #home page
    path('', views.index, name='index'),

    #show all pizzas
    path('pizza_list', views.pizza_list, name='pizza_list'),

    #toppings for each pizza
    path('pizza_list/<int:pizza_id>/', views.pizza, name='pizza'),

    path('new_pizza/', views.new_pizza, name='new_pizza'),

    path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment')
]