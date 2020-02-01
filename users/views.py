from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from  django.core.mail import send_mail


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
        send_mail("Hello "+username, "Thank you for signing up for Django Blog APP! you are now part of our blog",
                  "letssharethoughts123@gmail.com", [email], fail_silently=False)
        messages.success(request, f'You are successfully registered!')
        return redirect('login')

    return render(request, 'users/registration_form.html')


def profile(request):
    user = request.user.id
    user_profile = Profile.objects.get(user=user)
    if request.method == 'POST':

        profile_pic = request.POST.get('user_profile')
        profile.user = user
        profile.image = profile_pic
        return redirect('profile')
    return render(request, 'users/profile.html', {'user_profile': user_profile}
                  )


def update_details(request):
    if request.method == 'POST':
        user = request.user.id
        current_user = User.objects.get(id=user)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.email = email
        current_user.username = username
        current_user.save()
        return redirect('profile')


def update_profile(request, pk):
    if request.method == 'POST':
        user_profile_id = pk

        profile_pic = request.FILES.get('profile_image')
        fs = FileSystemStorage('media/profile_pics/')
        filename = fs.save(profile_pic.name, profile_pic)
        file_url = "profile_pics/"+filename
        updated_profile = Profile.objects.filter(id=user_profile_id)
        updated_profile.update(image=file_url)
        return redirect('profile')



