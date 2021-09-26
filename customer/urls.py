from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers_home, name='customers_home'),
    path('create', views.create, name='create_customer'),
    path('<int:pk>', views.customerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/update', views.customerUpdateView.as_view(), name='customers-update'),
    path('<int:pk>/delete', views.customerDeleteView.as_view(), name='customers-delete'),
]