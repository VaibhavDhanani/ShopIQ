from django.urls import path,include
from . import views

urlpatterns = [
    path("sign-up/",views.signUpUser,name="sign-up"),
    path("user/",views.userProfilePage,name="user-profile"),
    path("user/cart/",include("Cart.urls")),
]