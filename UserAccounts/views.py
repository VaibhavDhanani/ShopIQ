from django.shortcuts import render,redirect
from .forms import CustomUserForm
# Create your views here.
def signUpUser(request):
    if request.session.get('user_name'):
        previous_url = request.META.get('HTTP_REFERER', '/')  # '/' is the fallback if no referrer
        return redirect(previous_url)
    if(request.method == 'POST'):
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            request.session['user_name'] = form.cleaned_data.get('name')
            request.session['user_email'] = form.cleaned_data.get('email')
            request.session['user_type'] = form.cleaned_data.get('type')
            user.save()
            return redirect("home")
    else:
        form=CustomUserForm()
            
    context={'form':form}
    return render(request,"signup-form.html",context)


def userProfilePage(request):
    pass