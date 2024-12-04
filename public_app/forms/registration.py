from django.contrib.auth.models import User
from django.forms import ModelForm

from public_app.models import Profile


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        # fields = ('__all__')
        # exclude = ('is_superuser',)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


