from django.shortcuts import render
from django.views import View

from public_app.models import Post


class AboutView(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).all()
        contex = {'title': 'Ухххууу!', 'posts': posts}
        return render(request, 'about_page.html', contex)
