from django.urls import path,include
from . import views

urlpatterns = [
    path("sign-up/",views.signUpUser,name="sign-up"),
    path("log-in/",views.logInUser,name="log-in"),
    path("log-out/",views.logOutUser,name="log-out"),
    path("user/",views.userProfilePage,name="user-profile"),
    path("user/cart/",include("Cart.urls")),
]