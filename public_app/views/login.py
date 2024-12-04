from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from public_app.forms.login import LoginUserForm


class LoginView(View):
    @staticmethod
    def get(request):
        form = LoginUserForm()
        context = {
            'auth_form': form,
        }
        return render(request, 'auth_form.html', context)

    @staticmethod
    def post(request):
        form = LoginUserForm(request.POST)
        error = False

        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)

            if user is not None:
                login(request, user)

                next_page = request.GET.get('next', '/')
                return redirect(next_page)

            error = True

        context = {
            'auth_form': form,
            'error': error
        }

        return render(request, 'auth_form.html', context)