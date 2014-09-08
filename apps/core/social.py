from django.contrib.auth import get_user_model


def create_user(strategy, details, user=None, *args, **kwargs):
    strategy.session_get('key')
    if user:
        return {'is_new': False}

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
    return {
        'is_new': True,
        'user': user
    }
