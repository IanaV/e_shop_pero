from django.urls import path
from . import views

urlpatterns = [
    path('', views.sellers_home, name='sellers_home'),
    path('create_seller', views.create, name='create_seller'),
    path('<int:pk>', views.sellerDetailView.as_view(), name='seller-detail'),
    path('<int:pk>/update', views.sellerUpdateView.as_view(), name='sellers-update'),
    path('<int:pk>/delete', views.sellerDeleteView.as_view(), name='sellers-delete'),
]