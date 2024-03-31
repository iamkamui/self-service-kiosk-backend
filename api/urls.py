from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views

router = routers.DefaultRouter()
urlpatterns = list()

router.register(
    r"{0}".format(views.OrderViewSet.CustomMeta.base_url),
    views.OrderViewSet,
    basename="order",
)

core_urlpatterns = [
    path("", include((router.urls, "api"))),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += core_urlpatterns
