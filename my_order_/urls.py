from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_home, name='orders_home'),
    path('create_order', views.create, name='create_order'),
    path('<int:pk>', views.orderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update', views.orderUpdateView.as_view(), name='orders-update'),
    path('<int:pk>/delete', views.orderDeleteView.as_view(), name='orders-delete'),
]