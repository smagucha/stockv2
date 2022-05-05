from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('ProductCreate/', views.ProductCreate.as_view(), name='ProductCreate'),
    path('ProductUpdate/<int:pk>/', views.ProductUpdate.as_view(), name='ProductUpdate'),
    path('DeleteProduct/<int:pk>/', views.DeleteProduct.as_view(), name='DeleteProduct'),
    path('CategoryList/', views.CategoryList.as_view(), name='CategoryList'),
    path('CategoryCreate/', views.CategoryCreate.as_view(), name='CategoryCreate'),
    path('CategoryUpdate/<int:pk>/', views.CategoryUpdate.as_view(), name='CategoryUpdate'),
    path('DeleteCategory/<int:pk>/', views.DeleteCategory.as_view(), name='DeleteCategory'),
    path('AddProductQuantity/<int:pk>/', views.AddProductQuantity.as_view(), name='AddProductQuantity'),
    path('HighStockProduct/', views.HighStockProduct.as_view(), name='highstock'),
    path('LowStockProduct/', views.LowStockProduct.as_view(), name='less_stock'),
    path('SalePdfView/', views.SalePdfView.as_view(), name='SalePdfView'),
    path('render_pdf_view/<str:start_date>/<str:end_date>', views.render_pdf_view, name='render_pdf_view'),
]
