from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllProduct, name='all-products'),
    path('create-product/', views.createProduct, name='create-product'),
    path('update-product/<str:pk>/', views.updateProduct, name='update-product'),
    path('delete-product/<str:pk>/', views.deleteProduct, name='delete-product'),
]
