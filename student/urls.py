from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('my-orders/', views.my_orders, name='my_orders'),
]