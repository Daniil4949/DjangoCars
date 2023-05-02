from django.urls import path
from autoshow.views import AutoShowProfile, AutoModels

urlpatterns = [
    path("autoshows/", AutoShowProfile.as_view({"get": "list"}), name='All autoshows'),
    path("autoshows/<int:pk>/", AutoShowProfile.as_view({"get": "retrieve"})),
    path("autoshows/change-profile/", AutoShowProfile.as_view({"patch": "update"})),
    path("cars/", AutoModels.as_view({"get": "list", "post": "create"}), name='getting all desirable autos of the autoshow'),
    path("cars/<int:pk>/", AutoModels.as_view({"get": "retrieve"}),
         name='getting data about the definite desirable car')

]
