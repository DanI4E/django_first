from django.urls import path

from public_app.views.change_user import change_user
from public_app.views.about import AboutView
from public_app.views.create_post import CreatePostView
from public_app.views.login import login_user
from public_app.views.main_page import MainPageView
from public_app.views.photo import PhotoView
from public_app.views.profile import get_user_profile
from public_app.views.registration import RegistrationView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('about/', AboutView.as_view(), name='about'),
    path('photo/', PhotoView.as_view(), name='photo'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('login/', login_user, name='login'),
    path('profile/<int:id>/', get_user_profile, name='profile'),
    path("change_user/<int:id>/", change_user, name='change_user'),
    # path('logout/', logout_user, name='logout'),
]