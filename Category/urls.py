from django.urls import path
from . import views

urlpatterns = [
    path('',views.ShowAllCategoryWiseProducts,name = 'all-category-products'),
    path('<slug:catslug>/',views.ShowCategoryWiseProducts,name='category-product')
]