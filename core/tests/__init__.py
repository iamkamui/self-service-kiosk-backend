from typing import Dict, Optional

from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import Profile, User


class BaseTestAPI(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.start_order_endpoint = reverse("api:order-start")
        cls.user = cls.create_test_user()

    @classmethod
    def create_test_user(
        cls,
        username: str = "TestUser",
        email: str = "test_user@selfservicekiosk.com",
        first_name: str = "User",
        last_name: str = "Test",
    ) -> User:
        user = User(
            username=username, email=email, first_name=first_name, last_name=last_name
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
