from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_home, name='products_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.productsDetailView.as_view(), name='products-detail'),
    path('<int:pk>/update', views.productsUpdateView.as_view(), name='products-update'),
    path('<int:pk>/delete', views.productsDeleteView.as_view(), name='products-delete'),
]