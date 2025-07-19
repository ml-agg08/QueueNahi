from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from chef.models import MenuItem, Order
from users.models import UserProfile
from .forms import MenuItemForm
from django.contrib import messages

@login_required
def chef_queue(request):

    print("helllooo", flush=True)

    pending_orders = Order.objects.filter(status='pending').order_by('timestamp')
    completed_orders = Order.objects.filter(status='completed').order_by('-timestamp')

    print("hello")

    print(pending_orders)
    print(completed_orders)

    return render(request, 'test.html', {
        'pending_orders': pending_orders,
        'completed_orders': completed_orders
    })



@login_required
def mark_order_completed(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if UserProfile.objects.get(user=request.user).role == 'chef':
        order.status = 'completed'
        order.save()
    return redirect('chef_dashboard_2')


@login_required
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chef_dashboard_2')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

