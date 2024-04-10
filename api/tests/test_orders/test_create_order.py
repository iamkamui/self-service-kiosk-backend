import ipdb  # noqa

from api.utils.choices import OrderConsumptionChoices
from core.tests import BaseTestAPI


class TestCreateOrderAPI(BaseTestAPI):
    def test_create_order_with_anonymous_user(self):
        data = {"consumption": OrderConsumptionChoices.TAKE_HOME}
        response = self.client.post(self.start_order_endpoint, data=data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["products"]["products"], [])
        self.assertEqual(response.json()["user"], None)

    def test_create_order_with_authenticated_user(self):
        headers = self.get_authentication_header()
        data = {"consumption": OrderConsumptionChoices.EAT_IN}
        response = self.client.post(
            self.start_order_endpoint, data=data, headers=headers, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["products"]["products"], [])
        self.assertEqual(response.json()["user"], self.user.id)
    
    def test_create_order_without_consumption_option_raise_400(self):
        response = self.client.post(self.start_order_endpoint, format="json")
        self.assertEqual(response.status_code, 400)
