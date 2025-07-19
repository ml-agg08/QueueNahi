from django.urls import path
from . import views

urlpatterns = [
    path('chefdashboard/',views.chef_queue,name="chef_dashboard_2"),
    path('order/complete/<int:order_id>/', views.mark_order_completed, name='mark_order_completed'),
    path('add-menu-item/', views.add_menu_item, name='add_menu_item'),
]
