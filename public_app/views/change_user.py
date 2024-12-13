from django.contrib.auth.models import User

from django.shortcuts import render
from django.views import View

from public_app.models import Profile


# class ChangeUserView(View):
def change_user(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        profile.telegram_link = request.POST.get("telegram_link")
        user.save()
        profile.save()
        return render(request, 'profile.html', {"user": user})
    else:
        return render(request, "change_user_page.html", {"user": user})




    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data['password'])
    #
    #     if commit:
    #         user.save()
    #
    #     return user