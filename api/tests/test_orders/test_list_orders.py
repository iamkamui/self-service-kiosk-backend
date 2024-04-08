from core.tests import BaseTestAPI


class TestListOrderAPI(BaseTestAPI):
    def setUp(self) -> None:
        self.admin_user = self.create_test_user(is_superuser=True)
        self.admin_headers = self.get_authentication_header(self.admin_user)

    def test_list_order_with_admin_user_return_all_orders(self):
        pass

    def test_list_order_with_common_user_return_only_own_orders(self):
        pass

    def test_list_order_with_anonymous_user_return_only_own_orders_by_session(self):
        pass
