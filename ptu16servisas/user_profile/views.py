from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpRequest

User = get_user_model()

@csrf_protect
def signup(request: HttpRequest):
    if request.method == 'POST':
        errors = []
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or User.objects.filter(username=username).exists():
            errors.append('Username is taken, or is required')
        if not email or User.objects.filter(email=email).exists():
            errors.append('Email is taken, or is required')
        if not password1:
            errors.append('Password is required')
        if not password2:
            errors.append('Password confirmation is required')
        if password1 != password2:
            errors.append('Passwords do not match')

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1)
            messages.success(request, 'Account successfully created')
            return redirect('login')

    return render(request, 'registration/user_profile/signup.html')
