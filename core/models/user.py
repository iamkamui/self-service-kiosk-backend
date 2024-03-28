from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field import modelfields


class User(AbstractUser):
    email = models.EmailField(
        "email address",
        blank=True,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = modelfields.PhoneNumberField(
        "phone number", blank=False, unique=True
    )
    billing_address = models.CharField(
        "billing address", blank=True, max_length=255, null=True
    )
    delivery_address = models.CharField(
        "delivery address", blank=True, max_length=255, null=True
    )
