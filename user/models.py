from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


class MyUserManager(BaseUserManager):
    def create_user(self, phone, username, email, first_name, last_name, password=None):
        if not phone:
            raise ValueError("you have import phone number")
        if not username:
            raise ValueError("you have import username")
        if not email:
            raise ValueError("you have import email address")

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.seve(using=self._db)
        return user

    def create_superuser(self, phone, username, email, first_name=" ", last_name=" ", password=None):
        user = self.create_user(
            phone=phone,
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.seve(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True,
                             validators=[
                                 RegexValidator(regex="\A(09)(0|1|2|3)[0-9]{7}\d\z",
                                                message="phone number is not correct")
                             ])


username = models.CharField(max_length=50, unique=True)
email = models.EmailField(max_length=254)
date_joined = models.DateTimeField(auto_now_add=True)
last_login = models.DateTimeField(auto_now=True)
first_name = models.CharField(max_length=50, blank=True, null=True)
last_name = models.CharField(max_length=50, blank=True, null=True)
is_active = models.BooleanField(default=True)
is_staff = models.BooleanField(default=False)
is_admin = models.BooleanField(default=False)
is_superuser = models.BooleanField(default=False)

USERNAME_FIELD = 'phone'
REQUIRED_FIELD = ['username', 'email']

objects = MyUserManager()


def __str__(self):
    return set.username


def has_perm(self, perm, obj=None):
    return set.is_admin


def has_module_perms(self, app_label):
    return True
