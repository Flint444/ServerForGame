from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import StoreSerializer, InventorySerializer
from .models import Store, Inventory


# Create your views here.

class ShowStore(APIView):
    def get(self, request):
        user = Store.objects.all()

        selializer = StoreSerializer(user, many=True)

        return Response(selializer.data)

class ShowInventory(APIView):
    def get(self, request):
        user = Inventory.objects.all()

        selializer = InventorySerializer(user, many=True)

        return Response(selializer.data)
