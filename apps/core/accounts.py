from django.contrib.auth.models import User


class EmailOrUsernameModelBackend(object):

    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            users = User.objects.filter(**kwargs)
            for user in users:
                if user.check_password(password):
                    return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None