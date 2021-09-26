from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderUpdateForm

from django.views.generic import DetailView, UpdateView, DeleteView


def orders_home(request):
    orders = Order.objects.all()
    return render(request, 'my_order_/orders_home.html', {'orders': orders})


class orderDetailView(DetailView):
    model = Order
    template_name = 'my_order_/details_view.html'
    context_object_name = 'orders'


class orderUpdateView(UpdateView):
    model = Order
    template_name = 'my_order_/create_order.html'

    form_class = OrderUpdateForm



class orderDeleteView(DeleteView):
    model = Order
    success_url = '/orders/'
    template_name = 'my_order_/orders-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders_home')
        else:
            error = 'Форма была неверной'

    form = OrderUpdateForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'my_order_/create_order.html', data)
