from random import randint
from typing import Dict, Optional

from django.db.utils import IntegrityError
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import Profile, User
from core.tests.utils.builders import FakeProductBuild


class BaseTestAPI(APITestCase):
    """
    The BaseTestAPi provides a way to create test users and get authentication headers.
    By default it creates a test user without a admin permission.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.start_order_endpoint = reverse("api:orders-start")
        cls.list_order_endpoint = reverse("api:orders-list")
        cls.create_or_list_products_endpoint = reverse("api:products-list")
        cls.user = cls.create_test_user()
        cls.admin_user = cls.create_test_user(is_superuser=True)
        cls.builder = FakeProductBuild()

    @classmethod
    def create_test_user(
        cls,
        username: str = "TestUser",
        email: str = "test_user@selfservicekiosk.com",
        first_name: str = "User",
        last_name: str = "Test",
        is_superuser: bool = False,
    ) -> User:

        if is_superuser:
            username = f"{username}Admin"
            email = "test_user_admin@selfservicekiosk.com"
            last_name = f"{last_name}Admin"

        user, _ = User.objects.get_or_create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_superuser=is_superuser,
        )
        user.set_password("Testuserp@ssword")
        user.save()

        success = False

        while success is False:
            try:
                profile, _ = Profile.objects.get_or_create(
                    user=user, phone_number=f"+55{str(randint(10, 99))}900000000"
                )
                success = True
            except IntegrityError:
                continue

        return user

    @classmethod
    def get_authentication_header(cls, user: Optional[User] = None) -> Dict:
        if not user:
            user = cls.user

        refresh_token = RefreshToken.for_user(user)
        token = "Bearer {}".format(refresh_token.access_token)
        return {"Content-Type": "application/json", "Authorization": token}

    def populate(self, qt: int = 10):
        for i in range(qt):
            self.builder.build()
