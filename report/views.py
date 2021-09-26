
from django.shortcuts import render, redirect

# from .forms import ReportForm1
from os import path
import sys,os
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from customer.models import Customer

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from seller.models import Seller

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from product.models import Product

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from my_order_.models import Order


from .forms import ReportForm1,ReportForm2,ReportForm3
# from ..customer.models import Customer

def no_duplicate(qs_obj):
    """
    Функция отсекающая дубликаты, принемает параметер QuerySet
    кторой являеться результатом Model.objects.get(), Model.objects.all(), Model.objects.filter() и т.д
    """
    result = []
    ids = []
    for i in qs_obj:
        if i.pk not in ids:
            ids.append(i.pk)
            result.append(i)
    return result

from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.

def report(request):
    """Отображение всех покупателей заданного продавца"""
    # if not request.user.is_authenticated:
    #     return redirect('/auth/login')
    form = ReportForm1()
    # list_customer = Customer.objects.filter(order__seller__pk=request.POST.get('seller'))
    list_customer = Customer.objects.filter(order__seller__pk=request.POST.get('seller'))
    list_customer = no_duplicate(list_customer)  # Отсекаем дубликаты
    return render(request, 'report/report_1.html', {'form': form, 'list_customer': list_customer})


def report_2(request):
    """ Отображение всех продавцов, которые продали заданный товар"""
    # if not request.user.is_authenticated:
    #     return redirect('/auth/login')
    form = ReportForm2()
    list_seller = Seller.objects.filter(order__product__pk=request.POST.get('product'))
    list_seller = no_duplicate(list_seller)
    return render(request, 'report/report2.html', {'form': form, 'list_seller': list_seller})

def report_3(request):
    """ Отображение всех покупателей, которые купили заданный товар"""
    # if not request.user.is_authenticated:
    #     return redirect('/auth/login')
    form = ReportForm2()
    list_customer = Customer.objects.filter(order__product__pk=request.POST.get('product'))
    list_customer = no_duplicate(list_customer)
    return render(request, 'report/report2.html', {'form': form, 'list_seller': list_customer})


def report_4(request):
    """Отображение всех продаж на заданную дату"""
    # if not request.user.is_authenticated:
    #     return redirect('/auth/login')
    form = ReportForm3()
    list_date = Product.objects.filter(order__date=request.POST.get('date'))
    list_date = no_duplicate(list_date)
    return render(request, 'report/report4.html', {'form': form, 'list_date': list_date})

def report_5(request):
    """Отображение общей суммы продаж в заданный день."""
    # if not request.user.is_authenticated:
    #     return redirect('/auth/login')
    form = ReportForm3
    list_total = Order.objects.filter(date=request.POST.get('date'))
    list_total = no_duplicate(list_total)
    result_total = []
    for t in list_total:
        result_total.append(t.total)
    return render(request, 'report/report5.html', {'form': form, 'total': sum(result_total)})


