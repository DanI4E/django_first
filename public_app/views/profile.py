from django.contrib.auth.models import User
from django.shortcuts import render


def get_user_profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'profile.html', {"user": user})