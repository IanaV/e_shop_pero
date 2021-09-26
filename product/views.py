from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductUpdateForm
from django.views.generic import DetailView, UpdateView, DeleteView


def products_home(request):
    products = Product.objects.order_by('-name')
    return render(request, 'product/products_home.html', {'products': products})


class productsDetailView(DetailView):
    model = Product
    template_name = 'product/details_view.html'
    context_object_name = 'product'


class productsUpdateView(UpdateView):
    model = Product
    template_name = 'product/create.html'

    form_class = ProductUpdateForm


class productsDeleteView(DeleteView):
    model = Product
    success_url = '/products/'
    template_name = 'product/products-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_home')
        else:
            error = 'Форма была неверной'

    form = ProductUpdateForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'product/create.html', data)
