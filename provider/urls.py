from django.urls import path, include
from provider.views import ProviderProfile

urlpatterns = [
    path("providers/", ProviderProfile.as_view({"get": "list"}), name='All providers'),
    path("providers/<int:pk>/", ProviderProfile.as_view({"get": "retrieve"})),
    path("providers/change-profile/", ProviderProfile.as_view({"patch": "update"})),

]
