from rest_framework import viewsets
from Cars.permissions import ProviderPermission
from users.models import Provider
from provider.serializers import ProviderSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ProviderList(ListAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class DefineProvider(RetrieveAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class UpdateProvider(viewsets.ModelViewSet):
    http_method_names = ["get", "patch"]
    permission_classes = [ProviderPermission]
    serializer_class = [ProviderPermission]
    queryset = Provider.objects.all()

    def get_queryset(self):
        return Provider.objects.filter(user=self.request.user)

# class ProviderProfile(viewsets.ViewSet):
#     serializer_class = ProviderSerializer
#
#     @action(methods=["get"], detail=True)
#     def list(self, request):
#         providers_data = Provider.objects.all()
#         providers_data = ProviderSerializer(providers_data, many=True)
#         return Response(providers_data.data)
#
#     @action(methods=["get"], detail=True)
#     def retrieve(self, request, pk=None):
#         provider_data = get_object_or_None(Provider, pk=pk)
#         if provider_data:
#             provider_data = ProviderSerializer(provider_data, many=False)
#             return Response(provider_data.data)
#         else:
#             return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
#
#     @action(methods=["patch"], detail=True)
#     @permission_classes([ProviderPermission])
#     def update(self, request):
#         serializer = ProviderSerializer(data=request.data)
#         if serializer.is_valid():
#             provider_data = Provider.objects.get(user=self.request.user)
#             provider_data.name = request.data["name"]
#             provider_data.year_of_foundation = request.data["year_of_foundation"]
#             provider_data.save()
#             return Response(ProviderSerializer(provider_data).data)
#         else:
#             return Response("Data is not valid", status=status.HTTP_400_BAD_REQUEST)
