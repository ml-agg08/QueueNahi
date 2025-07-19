from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from chef.models import MenuItem, Order

from django.contrib import messages
from datetime import date
from chef.models import KitchenCapacity, MenuItem, Order

from chef.models import KitchenCapacity
from datetime import date

@login_required
def menu_view(request):
    menu_items = MenuItem.objects.all()
    capacity, _ = KitchenCapacity.objects.get_or_create(date=date.today())

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))

        try:
            item = MenuItem.objects.get(id=item_id)
        except MenuItem.DoesNotExist:
            messages.error(request, "Menu item not found.")
            return redirect('menu')

        # ❗ Strict check: deny if capacity is full
        if capacity.used_capacity >= capacity.max_capacity:
            messages.error(request, "Sorry, kitchen capacity has been reached for today.")
            return redirect('menu')

        # ❗ Deny if requested quantity is more than available
        if quantity > capacity.available_capacity():
            messages.error(request, f"Only {capacity.available_capacity()} meals left for today.")
            return redirect('menu')

        # ✅ Safe to place order
        Order.objects.create(student=request.user, menu_item=item, quantity=quantity)
        capacity.used_capacity += quantity
        capacity.save()

        messages.success(request, f"Order placed for {item.name} (x{quantity})")
        return redirect('my_orders')

    return render(request, 'menu.html', {
        'menu_items': menu_items,
        'capacity': capacity
    })



@login_required
def my_orders(request):
    orders = Order.objects.filter(student=request.user).order_by('-timestamp')
    return render(request, 'my_orders.html', {'orders': orders})
