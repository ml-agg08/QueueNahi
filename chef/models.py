from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.menu_item.name} x {self.quantity} - {self.student.username}'
    

from django.db import models
from datetime import date

class KitchenCapacity(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    max_capacity = models.PositiveIntegerField(default=200)
    used_capacity = models.PositiveIntegerField(default=0)

    def available_capacity(self):
        return self.max_capacity - self.used_capacity

    def __str__(self):
        return f"{self.date} - {self.used_capacity}/{self.max_capacity}"
