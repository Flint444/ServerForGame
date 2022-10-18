from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'password', 'balance', 'record']

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
        fields = ['nickname', 'record']

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'balance']
    def update(self, instance, validated_data):
        instance.balance += validated_data.get("balance", instance.balance)
        instance.save()
        return instance


