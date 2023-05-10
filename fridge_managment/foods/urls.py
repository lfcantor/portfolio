from django.urls import path
from .views import foodListView, foodCreateView, foodDeleteView

app_name = 'Foods'

urlpatterns = [
    path('', foodListView.as_view(), name='food_list'),
    path('add/', foodCreateView.as_view(), name='food_add'),
    path('<int:pk>/delete/', foodDeleteView.as_view(), name='food_delete'),
]