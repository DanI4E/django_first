from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from public_app.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    # sender - класс, модель пользователя, можем получить эту модель пользователя и что-то с этой моделью сделать,
    # хоть зарегистрироварть сразу несколько пользователей
    # instance - объект класса, тот самый пользователь который пойдёт в базу данных, или уже есть,
    # в зависимости какой сигнал
    # created - для понимания было ли редактирование или создание нового пользователя
    if not created:
        return

    profile = Profile(user=instance)
    # instance - это пользователь который есть в бд
    profile.save()
