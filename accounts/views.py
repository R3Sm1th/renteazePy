from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists, please login or register with username ")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email is already in use")
                    return redirect('register')
                else:
                  user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                  auth.login(request, user)
                  messages.success(request, 'You are now logged in')
                  return redirect('index')
        else:
            messages.error(request, 'Passwords dont match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
        else:
            messages.error(request, "Invalid login details")
            return redirect('register')
        return redirect('dashboard')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
