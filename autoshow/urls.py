from django.urls import path, include
# from autoshow.views import AutoShowProfile, AutoModels
from autoshow.views import AutoShowLists, DefineAutoShow, UpdateAutoShow
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", UpdateAutoShow)

urlpatterns = [
    path("autoshows/", AutoShowLists.as_view(), name="all-autoshows"),
    path("autoshows/<int:pk>/", DefineAutoShow.as_view(), name="define-autoshow"),
    path("update-autoshow/", include(router.urls), name="updating-profile"),

]
