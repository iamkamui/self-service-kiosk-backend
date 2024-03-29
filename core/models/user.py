from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field import modelfields


class User(AbstractUser):
    email = models.EmailField(
        "email address",
        blank=False,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    def __str__(self) -> str:
        return self.get_full_name()


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
