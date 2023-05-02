from django.urls import path
from customer.views import CustomerProfile

urlpatterns = [
    path("providers/", CustomerProfile.as_view({"get": "list"}), name='All customers'),
    path("providers/<int:pk>/", CustomerProfile.as_view({"get": "retrieve"})),
    path("providers/change-profile/", CustomerProfile.as_view({"patch": "update"})),

]
