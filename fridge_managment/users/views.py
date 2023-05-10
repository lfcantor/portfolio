from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import user
from django.urls import reverse_lazy

class UserListView(ListView):
    model = user
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = user 
    fields = ['Name']

class UserDeleteView(DeleteView):
    model = user
    success_url = reverse_lazy('users:user_list')


