from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import StoreSerializer, InventorySerializer
from .models import Store, Inventory


# Create your views here.

class ShowStore(APIView):
    def get(self, request):
        user = Store.objects.order_by('title')

        selializer = StoreSerializer(user, many=True)

        return Response(selializer.data)

class ShowInventory(APIView):
    def get(self, request):
        user = Inventory.objects.all()

        selializer = InventorySerializer(user, many=True)

        return Response(selializer.data)

class Buy(APIView):
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
