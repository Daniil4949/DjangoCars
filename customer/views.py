from rest_framework import viewsets, status
from Cars.permissions import CustomerPermission
from users.models import Provider
from customer.serializers import CustomerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from annoying.functions import get_object_or_None
from rest_framework.decorators import permission_classes
from users.models import Customer


class CustomerProfile(viewsets.ViewSet):
    serializer_class = CustomerSerializer

    @action(methods=["get"], detail=True)
    def list(self, request):
        customer_data = Customer.objects.all()
        customer_data = CustomerSerializer(data=customer_data, many=True)
        return Response(customer_data.data)

    @action(methods=["get"], detail=True)
    def retrieve(self, request, pk=None):
        customer_data = get_object_or_None(Customer, pk=pk)
        if customer_data:
            customer_data = CustomerSerializer(customer_data, many=False)
            return Response(customer_data.data)
        else:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

    @action(methods=["patch"], detail=True)
    @permission_classes([CustomerPermission])
    def update(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = Customer.objects.get(user=self.request.user)
            customer.name = request.data["name"]
            customer.save()
            return Response(CustomerSerializer(customer).data)
        else:
            return Response("Data is not valid", status=status.HTTP_400_BAD_REQUEST)
