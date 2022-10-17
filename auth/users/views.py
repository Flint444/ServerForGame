from django.shortcuts import render
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
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

        token = jwt.encode(payload, 'secret', algorithm='HS256')

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
        #user = User.objects.all()

        users = [User.nickname for User in User.objects.all()]
        records = [User.record for User in User.objects.all()]

        users_records = dict(zip(users, records))
        print(users_records)

        users_records = dict(sorted(users_records.items(), key=lambda item: item[1], reverse=True))
        print(users_records)


        #selializer = UserSerializer(users_records)

        #return Response(selializer.data)
        return Response(users_records)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Вы успешно вышли'
        }

        return response
