from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerUpdateForm

from django.views.generic import DetailView, UpdateView, DeleteView


def customers_home(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customers_home.html', {'customers': customers})


class customerDetailView(DetailView):
    model = Customer
    template_name = 'customer/details_view.html'
    context_object_name = 'customers'


class customerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer/create_customer.html'

    form_class = CustomerUpdateForm



class customerDeleteView(DeleteView):
    model = Customer
    success_url = '/customers/'
    template_name = 'customer/customers-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_home')
        else:
            error = 'Форма была неверной'

    form = CustomerUpdateForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'customer/create_customer.html', data)
