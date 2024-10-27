from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignUpForm, UserLogInForm


# Create your views here.
def signUpUser(request):
    if request.session.get("user_name"):
        previous_url = request.META.get("HTTP_REFERER", "/")
        return redirect(previous_url)
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            request.session["user_name"] = form.cleaned_data.get("name")
            request.session["user_email"] = form.cleaned_data.get("email")
            request.session["user_type"] = form.cleaned_data.get("type")
            user.save()
            return redirect("home")
    else:
        form = UserSignUpForm()

    context = {"form": form}
    return render(request, "signup-form.html", context)


def userProfilePage(request):
    pass


def logInUser(request):
    if request.session.get("user_name"):
        print(request.session.get("user_name"))
        previous_url = request.META.get("HTTP_REFERER", "/")
        return redirect(previous_url)

    if request.method == "POST":
        form = UserLogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            print(user)

            if user is not None:
                login(request, user)
                request.session["user_name"] = user.username
                request.session["user_email"] = user.email
                request.session["user_type"] = user.type
                previous_url = request.META.get("HTTP_REFERER", "/")
                return redirect(previous_url)
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = UserLogInForm()

    return render(request, "login-form.html", {"form": form})


def logOutUser(request):
    if request.session.get("user_name"):
        logout(request)
        request.session.flush()
    return redirect("home")
