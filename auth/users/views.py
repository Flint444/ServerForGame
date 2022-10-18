from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, BalanceSerializer, RecordSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Пользователь не найден!')

        if not user.check_password(password):
            raise AuthenticationFailed('Неверный пароль!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode("utf-8")

        response = Response({
            'jwt': token,
            'message': 'Вы успешно вошли'
        })

        response.set_cookie(key='jwt', value=token, httponly=True)
        response_data = {
            'jwt': token,
            'message': 'Вы успешно вошли'
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Не авторизован!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Не авторизован!')

        user = User.objects.filter(id = payload['id']).first()
        selializer = UserSerializer(user)

        return Response(selializer.data)

class UserRecords(APIView):
    def get(self, request):
        user = User.objects.order_by('-record')

        selializer = RecordSerializer(user, many=True)

        return Response(selializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Вы успешно вышли'
        }

        return response

class UpdateUserBalance(APIView):
    def put(self, request):
        user = User.objects.order_by('-balance')

        selializer = BalanceSerializer(user, many=True)

        return Response(selializer.data)
