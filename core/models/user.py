from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field import modelfields

from core.models import BaseModel


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


class Profile(BaseModel):
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

    def get_billing_address(self):
        return self.address_set.get(is_main_billing=True)

    def get_delivery_address(self):
        return self.address_set.get(is_main_delivery=True)


class Address(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    country = models.CharField("country", blank=False, null=False, max_length=150)
    zip_code = models.CharField("zip_code", blank=False, null=False, max_length=150)
    state = models.CharField("state", blank=False, null=False, max_length=150)
    street = models.CharField("street", blank=False, null=False, max_length=150)
    number = models.CharField("number", blank=False, null=False, max_length=150)
    complement = models.CharField("complement", blank=True, null=True, max_length=150)
    is_main_delivery = models.BooleanField("main delivery address", default=False)
    is_main_billing = models.BooleanField("main billing address", default=False)

    def __str__(self) -> str:
        return "{}, {} - {}".format(self.street, self.number, self.state)

    def set_main_delivery_address(self):
        current_main_delivery = self.profile.address_set.get(is_main_delivery=True)
        if current_main_delivery:
            current_main_delivery.is_main_delivery = False
            current_main_delivery.save()
        self.is_main_delivery = True
        self.profile.delivery_address = self.__str__()
        self.profile.save()
        return

    def set_main_billing_address(self):
        current_main_billing = self.profile.address_set.get(is_main_billing=True)
        if current_main_billing:
            current_main_billing.is_main_billing = False
            current_main_billing.save()
        self.is_main_billing = True
        self.profile.billing_address = self.__str__()
        self.profile.save()
        return
