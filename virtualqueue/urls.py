from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('student/', include('student.urls')),
    path('chef/', include('chef.urls')),
]


