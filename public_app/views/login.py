from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from public_app.forms.login import LoginUserForm


# class LoginView(View):
    # def post(self, request):
    #     form = LoginForm(request.POST or None)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)  # Проверяем учетные данные
    #         if user is not None:
    #             login(request, user)
    #             return redirect('/')
    #     context = {
    #         'auth_form': form,
    #     }
    #     return render(request, 'auth_form.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return render(request, 'profile.html')
    else:
        form = LoginUserForm()
    return render(request, 'auth_form.html', {'form': form})