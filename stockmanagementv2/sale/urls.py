from django.urls import path
from . import views

urlpatterns = [
    path('', views.SaleList.as_view(), name='SaleList'),
    path('SaleCreate/', views.SaleCreate.as_view(), name='SaleCreate'),
    path('SaleUpdate/<int:pk>/', views.SaleUpdate.as_view(), name='SaleUpdate'),
    path('DeleteSale/<int:pk>/', views.DeleteSale.as_view(), name='DeleteSale'),
    path('OrderList', views.OrderList.as_view(), name='OrderList'),
    path('OrderCreate/', views.OrderCreate.as_view(), name='OrderCreate'),
    path('OrderDelete/<int:pk>/', views.OrderDelete.as_view(), name='OrderDelete')
]
