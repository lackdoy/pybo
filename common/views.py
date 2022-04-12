from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm

def signup(request):
    """
    회원가입
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})

# Create your views here.

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})