import ipdb  # noqa

from api.models import Product
from core.tests import BaseTestAPI


class TestListProductsAPI(BaseTestAPI):
    def setUp(self) -> None:
        self.populate()

    def test_list_products_with_admin_return_all_products(self):
        total_products = Product.objects.count()
        admin_headers = self.get_authentication_header(self.admin_user)
        response = self.client.get(
            self.create_or_list_products_endpoint, headers=admin_headers, format="json"
        )
        self.assertEqual(total_products, len(response.json()))

    def test_list_products_without_admin_return_only_active_products(self):
        total_products = Product.objects.all()

        Product.objects.filter(
            id__in=total_products.values_list("id", flat=True)[:3]
        ).update(is_active=False)

        total_actives_products = Product.active.count()

        user_response = self.client.get(
            self.create_or_list_products_endpoint, format="json"
        )

        admin_response = self.client.get(
            self.create_or_list_products_endpoint,
            headers=self.get_authentication_header(self.admin_user),
            format="json",
        )
        self.assertEqual(total_actives_products, len(user_response.json()))
        self.assertEqual(total_products.count(), len(admin_response.json()))
        self.assertLess(total_actives_products, total_products.count())
