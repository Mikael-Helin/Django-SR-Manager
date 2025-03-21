# authsr/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def sr_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authsr/login.html', {
                'error': 'Invalid credentials or not a superuser.'
            })

    return render(request, 'authsr/login.html')


@login_required
def sr_logout(request):
    logout(request)
    return redirect('sr_login')


@login_required
def home(request):
    return render(request, 'authsr/home.html', {'user': request.user})
