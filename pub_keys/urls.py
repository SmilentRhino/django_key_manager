from django.conf.urls import url, include
from pub_keys import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pub_keys', views.PublicKeyViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'add_key', views.add_key),
]
