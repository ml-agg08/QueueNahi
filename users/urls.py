from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import RoleBasedLoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', RoleBasedLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logoutpage ,name='logout'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('chef/dashboard/', views.chef_dashboard, name='chef_dashboard'),
]
