from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import RegisterUserForm, LoginUserForm



# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#         	form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Создан аккаунт {username}!')
#             return redirect('blog-home')
#         else:
#             form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан')
            
    else:
        form = RegisterUserForm()

    return render(request, 'reglog/registration.html', {'form' : form})

def login(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Вход выполнен')
    else:
        form = LoginUserForm()

    return render(request, 'reglog/login.html', {'form' : form})