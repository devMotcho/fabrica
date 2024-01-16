from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def loginView(request):
    """
    Criar sessão se o user existir 
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Something went wrong!', 'alert-warning alert-dismissible')


        user = authenticate(
            request,
            username=username,
            password=password
            )
            
        if user is not None:
            login(request, user)
            return redirect('dashboard:home')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('users:login')

