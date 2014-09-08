from django.db import models
from social.pipeline.user import create_user
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):

    # def create_user(self, email):
    #     return self.model._default_manager.create(email=email)

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    username = models.CharField(
        max_length=30,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(default=False)

    # last_login = models.DateTimeField(
    #     blank=True,
    #     null=True
    # )

    is_active = models.BooleanField(
        default=False
    )

    objects = CustomUserManager()

    def __unicode__(self):
        return self.username

    def is_authenticated(self):
        return True