from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from User_Password_Reset.basemodel import TimeBaseModel
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from .utils import send_raw_email, generate_four_random_numbers
# Create your models here.

class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if '@' and '.com' not in email:
            raise ValueError(_("Invalid email"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)            


class User(AbstractUser):
    username  = None
    email     = models.EmailField(_("email address"), unique=True)
    date_joined   = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name="last login", auto_now=True)

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = []

    objects = CustomerUserManager()

    def __str__(self):
        return self.email if self.email else ""
    

class UserEmailVerification(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_four_random_numbers()
        super().save(*args, kwargs)

    def __str__(self) -> str:
        return self.user.email    