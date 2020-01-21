from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
            user.set_password(password)
            user.save()
        messages.success(request, f'You are successfully registered!')
        return redirect('login')

    return render(request, 'users/register.html')





