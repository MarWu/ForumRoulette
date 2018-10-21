from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import UserInfo
# from .forms import UserCreationForm as CustomUserCreationForm


def index(request):
    return HttpResponse("Hello, world. You're at the users index.")


def profile(request, username):
    current_user = get_object_or_404(User, username=username)
    user_info = get_object_or_404(UserInfo, user_reference=current_user.id)
    return render(request, 'profile.html', {'selected_user': current_user, 'user_info': user_info})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_info = UserInfo(user_reference=user)
            user_info.save()
            return redirect('posts:index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
