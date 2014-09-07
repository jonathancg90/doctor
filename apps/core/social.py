from django.contrib.auth import get_user_model
from django.contrib import auth


def create_user(strategy, details, user=None, *args, **kwargs):
    email = details.get('email', None)
    user_model = get_user_model()
    try:
        user = user_model.objects.get(email=email)
    except user_model.DoesNotExist:
        user = user_model(
            username=email,
            email=email
        )
        user.save()
