from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return render(request, 'reglog/index.html')
    else:
        form = LoginForm()
    return render(request, 'reglog/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return render(request, 'reglog/index.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'reglog/registration.html', {'form': user_form})