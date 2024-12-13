from django import forms
from django.forms import ModelForm
from public_app.models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'text'
        ]
        # widgets = {
        #     'title': forms.TextInput(attrs={'placeholder': 'Заголовок', 'class': 'form-control'}),
        #     'images': forms.FileInput(attrs={'class': 'form-control', 'multiple': 'multiple'}),
        #     'text': forms.Textarea(attrs={'placeholder': 'Текст', 'class': 'form-control'})
        # }
        # labels = {
        #     'title': 'Заголовок',
        #     'images': 'Фотографии',
        #     'text': 'Текст',
        # }


