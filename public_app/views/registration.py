from django.shortcuts import render, redirect
from django.views import View

from public_app.forms.registration import RegistrationForm


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {
            'reg_form': form,
        }
        return render(request, 'registration_page.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'reg_form': form,
        }
        return render(request, 'registration_page.html', context)

