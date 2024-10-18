from django.urls import path
from . import views
urlpatterns = [
    path("",views.showCart,name="user-cart"),
    path("buy",views.buyUserItems,name="buy-user-items")
]