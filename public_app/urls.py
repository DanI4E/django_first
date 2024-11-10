from django.template.defaulttags import url
from django.urls import path

from public_app.views.about import AboutView
from public_app.views.login import login_user, logout_user
from public_app.views.main_page import MainPageView
from public_app.views.photo import PhotoView
from public_app.views.profile import ProfileView
from public_app.views.registration import RegistrationView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('about/', AboutView.as_view(), name='about'),
    path('photo/', PhotoView.as_view(), name='photo'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', login_user, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('logout/', logout_user, name='logout'),
]