from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')