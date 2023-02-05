from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True)

    first_name = models.CharField(
        max_length=30,
        blank=False,
        error_messages={'required': 'Le prénom est requis'}
    )

    last_name = models.CharField(
        max_length=150,
        blank=False,
        error_messages={'required': 'Le nom est requis'}
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
        error_messages={'required': 'L\'email est requis', 'unique': 'L\'email est déjà utilisé'}
    )

    mobile_phone = models.CharField(
        max_length=15,
        blank=False,
        validators=[RegexValidator(r'^\d{10,15}$', 'Le numéro de téléphone mobile n\'est pas valide')],
        error_messages={'required': 'Le numéro de téléphone mobile est requis'}
    )

    home_phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(r'^\d{10,15}$', 'Le numéro de téléphone fixe n\'est pas valide')])

    adress = models.CharField(
        max_length=255,
        blank=False,
        error_messages={'required': 'L\'adresse est requise'}
    )

    zip_code = models.CharField(
        max_length=10,
        blank=False,
        validators=[RegexValidator(r'^\d{5,10}$', 'Le code postal n\'est pas valide')],
        error_messages={'required': 'Le code postal est requis'}
    )

    city = models.CharField(
        max_length=100,
        blank=False,
        error_messages={'required': 'La ville est requise'}
    )

    country = models.CharField(
        max_length=50,
        blank=False,
        choices=(
            ('France', 'France'),
            ('Etats-Unis', 'Etats-Unis'),
            ('Angleterre', 'Angleterre'),
            ('Canada', 'Canada'),
        ),
        error_messages={'required': 'Le pays est requis'})

    kbis = models.CharField(
        max_length=100,
        blank=False,
        validators=[RegexValidator(r'^[0-9]{14}$', 'Le numéro de KBIS n\'est pas valide')],
        error_messages={'required': 'Le numéro de KBIS est requis'})

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
