from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Records
from .serializers import RecordSerializer


# Create your views here.

class ShowRecords(APIView):
    def get(self, request):
        records = Records.objects.all()

        serializer = RecordSerializer(records)
        return Response(serializer.data)