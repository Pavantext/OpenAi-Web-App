from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def LoginView(request):
    return render('login.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def home_view(request):
    return render(request, 'home.html')