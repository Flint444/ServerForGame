from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'balance', 'record']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'record']


class RegistrationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=50, min_length=4)
    email = serializers.EmailField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)

        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': ('email already exist')})
        if User.objects.filter(username = username).exists():
            raise serializers.ValidationError({'username': ('nickname already exist')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
