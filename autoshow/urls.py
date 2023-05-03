from django.urls import path, include
# from autoshow.views import AutoShowProfile, AutoModels
from autoshow.views import AutoShowLists, DefineAutoShow, UpdateAutoShow
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", UpdateAutoShow)

urlpatterns = [
    # path("autoshows/", AutoShowProfile.as_view({"get": "list"}), name='All autoshows'),
    # path("autoshows/<int:pk>/", AutoShowProfile.as_view({"get": "retrieve"})),
    # path("autoshows/change-profile/", AutoShowProfile.as_view({"patch": "update"})),
    # path("cars/", AutoModels.as_view({"get": "list", "post": "create"}), name='getting all desirable autos of the autoshow'),
    # path("cars/<int:pk>/", AutoModels.as_view({"get": "retrieve"}),
    #      name='getting data about the definite desirable car')
    path("autoshows/", AutoShowLists.as_view(), name="Getting all the autoshows"),
    path("autoshows/<int:pk>/", DefineAutoShow.as_view(), name="Getting define autoshow"),
    path("update-autoshow/", include(router.urls), name="updating profile"),

]
