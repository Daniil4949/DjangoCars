from django.urls import path, include
from provider.views import ProviderList, UpdateProvider, DefineProvider
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", UpdateProvider)

urlpatterns = [
    path("providers/", ProviderList.as_view(), name="All providers"),
    path("providers/<int:pk>/", DefineProvider.as_view(), name='Getting define provider by id'),
    path("update-provider/", include(router.urls), name="Updating profile")

]
