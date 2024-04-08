from typing import Dict, Optional

from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import Profile, User


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

    @classmethod
    def create_test_user(
        cls,
        username: str = "TestUser",
        email: str = "test_user@selfservicekiosk.com",
        first_name: str = "User",
        last_name: str = "Test",
        is_superuser: bool = False,
    ) -> User:
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_superuser=is_superuser,
        )
        user.set_password("Testuserp@ssword")
        user.save()

        Profile.objects.create(user=user, phone_number="+5521900000000")
        return user

    @classmethod
    def get_authentication_header(cls, user: Optional[User] = None) -> Dict:
        if not user:
            user = cls.user

        refresh_token = RefreshToken.for_user(user)
        token = "Bearer {}".format(refresh_token.access_token)
        return {"Content-Type": "application/json", "Authorization": token}
