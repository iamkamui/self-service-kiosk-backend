import ipdb  # noqa
from rest_framework.test import APIClient

from api.models import Order
from api.utils.choices import OrderConsumptionChoices
from core.tests import BaseTestAPI


class TestListOrderAPI(BaseTestAPI):
    def setUp(self) -> None:
        self.user_2 = self.create_test_user(
            username="TestUser2", email="test_user2@selfservicekiosk.com"
        )
        self.admin_headers = self.get_authentication_header(self.admin_user)
        self.user_headers = self.get_authentication_header(self.user)
        self.user_2_headers = self.get_authentication_header(self.user_2)
        self.__create_setup_orders()

    def __create_setup_orders(self, qt: int = 6):
        payload = {
            "data": {"consumption": OrderConsumptionChoices.TAKE_HOME},
            "format": "json",
        }

        initial_orders = Order.objects.count()
        payload["headers"] = self.user_headers

        for _ in range(int(qt / 2)):
            response = self.client.post(self.start_order_endpoint, **payload)  # noqa

        payload["headers"] = self.user_2_headers

        for _ in range(int(qt / 2)):
            response2 = self.client.post(self.start_order_endpoint, **payload)  # noqa

        total_orders = Order.objects.count()

        self.assertEqual(total_orders, initial_orders + qt)
        return

    def test_list_order_with_admin_user_return_all_orders(self):
        total_orders = Order.objects.count()
        response = self.client.get(
            self.list_order_endpoint, headers=self.admin_headers, format="json"
        )
        self.assertEqual(total_orders, len(response.json()))

    def test_list_order_with_common_user_return_only_own_orders(self):
        total_user1_orders = Order.objects.filter(user=self.user).count()
        response = self.client.get(
            self.list_order_endpoint, headers=self.user_headers, format="json"
        )

        for order in response.json():
            self.assertEqual(order["user"], self.user.id)

        self.assertEqual(total_user1_orders, len(response.json()))

    def test_list_order_with_anonymous_user_return_only_own_orders_by_session(self):
        total_orders = Order.objects.count()
        client = APIClient()

        response = client.get(self.list_order_endpoint, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)
        self.assertLess(len(response.json()), total_orders)

        creation_response = client.post(
            self.start_order_endpoint,
            data={"consumption": OrderConsumptionChoices.TAKE_HOME},
            format="json",
        )

        self.assertEqual(creation_response.status_code, 201)

        response2 = client.get(self.list_order_endpoint, format="json")
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(len(response2.json()), 1)
