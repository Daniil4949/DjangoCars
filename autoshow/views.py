from users.models import AutoShow, DesirableAuto
import rest_framework.viewsets as viewsets
from autoshow.serializers import AutoShowSerializer, AutoShowUpdateSerializer
from Cars.permissions import AutoShowPermission
from autoshow.serializers import DesirableAutoReadSerializer, DesirableAutoSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView


class AutoShowLists(ListAPIView):
    serializer_class = AutoShowSerializer
    queryset = AutoShow.objects.all()


class DefineAutoShow(RetrieveAPIView):
    serializer_class = AutoShowSerializer
    queryset = AutoShow.objects.all()


class UpdateAutoShow(viewsets.ModelViewSet):
    http_method_names = ["get", "patch"]
    permission_classes = [AutoShowPermission]
    serializer_class = AutoShowUpdateSerializer
    queryset = AutoShow.objects.all()

    def get_queryset(self):
        return AutoShow.objects.filter(user=self.request.user)


class AutoModels(ListAPIView):
    queryset = DesirableAuto.objects.all()
    serializer_class = AutoShowSerializer
    permission_classes = [AutoShowPermission]

    def get_queryset(self):
        return DesirableAuto.objects.filter(autoshow__user=self.request.user)


class DefineAutoModels(RetrieveAPIView):
    queryset = DesirableAuto.objects.all()
    serializer_class = DesirableAutoReadSerializer
    permission_classes = [AutoShowPermission]

    def get_queryset(self):
        return DesirableAuto.objects.filter(autoshow__user=self.request.user)


class CreateAutoModel(CreateAPIView):
    queryset = DesirableAuto.objects.all()
    serializer_class = DesirableAuto
    permission_classes = [AutoShowPermission]
