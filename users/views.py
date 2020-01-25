from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile


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
            Profile.objects.create(user=user)
        messages.success(request, f'You are successfully registered!')
        return redirect('login')

    return render(request, 'users/register.html')


def profile(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    if request.method == 'POST':

        profile_pic = request.POST.get('user_profile')
        profile.user = user
        profile.image = profile_pic
        return redirect('profile')
    return render(request, 'users/user_profile.html', {'user_profile': user_profile}
                  )


