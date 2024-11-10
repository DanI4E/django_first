from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get_user_profile(self, request, username):
        user = User.objects.get(username=username)
        return render(request, 'profile.html', {"user": user})