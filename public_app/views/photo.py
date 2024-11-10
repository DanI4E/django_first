from django.shortcuts import render
from django.views import View

from public_app.models import Post


class PhotoView(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=False).order_by('-created_at', '-id').all()
        contex = {'title': '123123123!', 'posts': posts}
        return render(request, 'photo_page.html', contex)