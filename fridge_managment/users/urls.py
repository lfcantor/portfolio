from django.urls import path
from .views import UserListView, UserCreateView, UserDeleteView

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_add'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]