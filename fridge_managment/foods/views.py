from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import food
from django.urls import reverse_lazy

class foodListView(ListView):
    model = food
    template_name = 'foods/food_list.html'
    context_object_name = 'foods'

class foodCreateView(CreateView):
    model = food 
    fields = ['Name']

class foodDeleteView(DeleteView):
    model = food
    success_url = reverse_lazy('foods:food_list')

    

