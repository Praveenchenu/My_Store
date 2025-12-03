from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm 



def Signup(request):
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username}, your registration is succesfully ")
            return redirect('app:home')
        else:
            print("form error")
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'users/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form  = AuthenticationForm(request=request,  data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('app:home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

    
def log_out(request):
    logout(request)
    return redirect('app:home')

@login_required
def profile(request):
    return render(request, 'users/profile.html')