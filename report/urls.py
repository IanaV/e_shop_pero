from django.urls import path
from . import views

urlpatterns = [


    path('', views.report, name='report'),
    path('report_2', views.report_2, name='report_2'),
    path('report_3', views.report_3, name='report_3'),
    path('report_4', views.report_4, name='report_4'),
    path('report_5', views.report_5, name='report_5'),
    # path('<int:pk>', views.productsDetailView.as_view(), name='products-detail'),
    # path('<int:pk>/update', views.productsUpdateView.as_view(), name='products-update'),
    # path('<int:pk>/delete', views.productsDeleteView.as_view(), name='products-delete'),
]