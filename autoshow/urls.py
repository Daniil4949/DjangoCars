from django.urls import path, include
from provider.views import ProviderProfile
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register(r"profile", ProviderProfile, basename="Provider profile")

urlpatterns = [
    # path("change/", include(router.urls), name="changing-profile"),
    # path("providers/", ProviderProfile.as_view({"get": "list"}), name='All providers'),
    # path("providers/<int:pk>/", ProviderProfile.as_view({"get": "retrieve"})),
    # path("providers/change-profile/", ProviderProfile.as_view({"patch": "update"})),

]
