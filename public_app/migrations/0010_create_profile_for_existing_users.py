from django.db import migrations


def create_profile_existing_users(apps, schema_editor):
    user_model = apps.get_model('auth', 'User') # User - модель пользователей
    profile_model = apps.get_model('public_app', 'Profile') # Profile - модель профилей

    users = user_model.objects.filter(profile__isnull=True).all()
    for user in users:
        profile = profile_model(user=user)
        profile.save()

    # profile_model.objects.bulk_create([{}, {}, {}]) - сигналы при bulk_create не работают,
    # так как bulk_create не использует save() внутри себя


class Migration(migrations.Migration):
    dependencies = [
        ('public_app', '0009_profile_about_profile_phone_number'),
    ]

    operations = (
        migrations.RunPython(create_profile_existing_users),
    )
