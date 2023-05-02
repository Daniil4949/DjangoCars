from users.models import AutoShow, DesirableAuto
from rest_framework.decorators import action
from rest_framework.response import Response
from annoying.functions import get_object_or_None
import rest_framework.viewsets as viewsets
from rest_framework import status
from autoshow.serializers import AutoShowSerializer, AutoShowUpdateSerializer
from rest_framework.decorators import permission_classes
from Cars.permissions import AutoShowPermission
from autoshow.serializers import DesirableAutoReadSerializer, DesirableAutoSerializer


class AutoShowProfile(viewsets.ViewSet):
    serializer_class = AutoShowSerializer

    @action(methods=["get"], detail=True)
    def list(self, request):
        autoshow_data = AutoShow.objects.all()
        autoshow_data = AutoShowSerializer(autoshow_data, many=True)
        return Response(autoshow_data.data)

    @action(methods=["get"], detail=True)
    def retrieve(self, request, pk=None):
        autoshow_data = get_object_or_None(AutoShow, pk=pk)
        if autoshow_data:
            autoshow_data = AutoShowSerializer(autoshow_data, many=False)
            return Response(autoshow_data.data)
        else:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

    @action(methods=["patch"], detail=True)
    @permission_classes([AutoShowPermission])
    def update(self, request):
        serializer = AutoShowUpdateSerializer(data=request.data)
        if serializer.is_valid():
            autoshow_data = AutoShow.objects.get(user=self.request.user)
            autoshow_data.name = request.data["name"]
            autoshow_data.location = request.data["location"]
            autoshow_data.save()
            return Response(AutoShowUpdateSerializer(autoshow_data).data)
        else:
            return Response("Data is not valid", status=status.HTTP_400_BAD_REQUEST)


class AutoModels(viewsets.ViewSet):
    permission_classes = [AutoShowPermission]

    @action(methods=["get"], detail=True)
    def list(self, request):
        autoshow_data = DesirableAuto.objects.filter(autoshow=AutoShow.objects.get(user=self.request.user))
        autoshow_data = DesirableAutoSerializer(autoshow_data, many=True)
        return Response(autoshow_data.data)

    @action(methods=["post"], detail=True)
    def create(self, request):
        data = DesirableAutoSerializer(data=request.data, many=False)
        if data.is_valid():
            autoshow_item = AutoShow.objects.get(user=self.request.user)
            new_auto = DesirableAuto(mark=data["mark"],
                                     model=data["model"],
                                     price=data["price"],
                                     autoshow=autoshow_item)
            new_auto.save()
            return Response(AutoShowSerializer(autoshow_item, many=False))
        else:
            return Response("Not valid data", status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["list"], detail=True)
    def retrieve(self, request, pk=None):
        auto = get_object_or_None(DesirableAuto, pk=pk)
        if auto:
            auto = DesirableAutoReadSerializer(auto, many=False)
            return Response(auto.data)
        else:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)
