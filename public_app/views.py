from django.shortcuts import render

from .models import Post


# Create your views here.
def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
    contex = {'title': 'Добрый день!', 'posts': posts}
    return render(request, 'main_page.html', contex)


def about(request):
    posts = Post.objects.filter(is_public=True).all()
    contex = {'title': 'Ухххууу!', 'posts': posts}
    return render(request, 'about.html', contex)


def photo(request):
    posts = Post.objects.filter(is_public=False).order_by('-created_at', '-id').all()
    contex = {'title': '123123123!', 'posts': posts}
    return render(request, 'photo.html', contex)



