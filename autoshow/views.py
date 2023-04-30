from users.models import Provider
from provider.serializers import ProviderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from annoying.functions import get_object_or_None
import rest_framework.viewsets as viewsets
from rest_framework import status


class ProviderProfile(viewsets.ViewSet):
    serializer_class = ProviderSerializer

    @action(methods=["get"], detail=True)
    def list(self, request):
        providers_data = Provider.objects.all()
        providers_data = ProviderSerializer(providers_data, many=True)
        return Response(providers_data.data)

    @action(methods=["get"], detail=True)
    def retrieve(self, request, pk=None):
        provider_data = get_object_or_None(Provider, pk=pk)
        if provider_data:
            provider_data = ProviderSerializer(provider_data, many=False)
            return Response(provider_data.data)

    @action(methods=["patch"], detail=True)
    def update(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            provider_data = Provider.objects.get(user=self.request.user)
            provider_data.name = request.data["name"]
            provider_data.year_of_foundation = request.data["year_of_foundation"]
            provider_data.save()
            return Response(ProviderSerializer(provider_data).data)
        else:
            return Response("Data is not valid", status=status.HTTP_400_BAD_REQUEST)
