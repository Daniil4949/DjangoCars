from django.urls import path, include
from customer.views import CustomerLists, DefineCustomer, UpdateCustomer
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", UpdateCustomer)

urlpatterns = [
    path("customers/", CustomerLists.as_view(), name="All customers"),
    path("customers/<int:pk>/", DefineCustomer.as_view(), name="Getting define customer by pk"),
    path("update-customer/", include(router.urls), name="updating profile")

]
