from rest_framework import viewsets, status
from Cars.permissions import CustomerPermission
from customer.serializers import CustomerSerializer
from users.models import Customer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class CustomerLists(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class DefineCustomer(RetrieveAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class UpdateCustomer(viewsets.ModelViewSet):
    http_method_names = ["get", "patch"]
    permission_classes = [CustomerPermission]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)

# class CustomerProfile(viewsets.ViewSet):
#     serializer_class = CustomerSerializer
#
#     @action(methods=["get"], detail=True)
#     def list(self, request):
#         customer_data = Customer.objects.all()
#         customer_data = CustomerSerializer(data=customer_data, many=True)
#         return Response(customer_data.data)
#
#     @action(methods=["get"], detail=True)
#     def retrieve(self, request, pk=None):
#         customer_data = get_object_or_None(Customer, pk=pk)
#         if customer_data:
#             customer_data = CustomerSerializer(customer_data, many=False)
#             return Response(customer_data.data)
#         else:
#             return Response("Not found", status=status.HTTP_404_NOT_FOUND)
#
#     @action(methods=["patch"], detail=True)
#     @permission_classes([CustomerPermission])
#     def update(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             customer = Customer.objects.get(user=self.request.user)
#             customer.name = request.data["name"]
#             customer.save()
#             return Response(CustomerSerializer(customer).data)
#         else:
#             return Response("Data is not valid", status=status.HTTP_400_BAD_REQUEST)
