from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register(
    r"{}".format(views.ProductViewset.CustomMeta.base_url),
    views.ProductViewset,
    basename="products",
)
urlpatterns = []
urlpatterns += router.urls
