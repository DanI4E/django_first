from django.forms import ModelForm
from public_app.models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


