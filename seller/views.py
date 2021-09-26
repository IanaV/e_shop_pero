from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Seller
from .forms import SellerUpdateForm

from django.views.generic import DetailView, UpdateView, DeleteView


def sellers_home(request):
    sellers = Seller.objects.all()
    return render(request, 'seller/sellers_home.html', {'sellers': sellers})


class sellerDetailView(DetailView):
    model = Seller
    template_name = 'seller/details_view.html'
    context_object_name = 'sellers'


class sellerUpdateView(UpdateView):
    model = Seller
    template_name = 'order/create_seller.html'

    form_class = SellerUpdateForm



class sellerDeleteView(DeleteView):
    model = Seller
    success_url = '/sellers/'
    template_name = 'seller/sellers-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = SellerUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellers_home')
        else:
            error = 'Форма была неверной'

    form = SellerUpdateForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'seller/create_seller.html', data)
