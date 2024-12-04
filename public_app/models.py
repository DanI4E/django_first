from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
import os
from uuid import uuid4


def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Post(models.Model):
    objects = None
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # related_name - аргумент, показывает как мы можем мз объекта пользователя обращаться к Profile
    avatar = models.ImageField(blank=True, null=True)
    phone_number = models.CharField(
        validators=[RegexValidator(regex=r'^((+7|7|8)+([0-9]){10})$')],
        max_length=17,
        blank=True,
        null=True,
    )
    about = models.TextField(max_length=4096, blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)

