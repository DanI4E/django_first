from django.shortcuts import redirect, render
from django.views import View

from public_app.forms.create_post import CreatePostForm


class CreatePostView(View):
    def get(self, request):
        form = CreatePostForm()
        context = {
            'create_form': form,
        }
        return render(request, 'create_post_page.html', context)

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        return render(request, 'create_post_page.html', {'create_form': form})