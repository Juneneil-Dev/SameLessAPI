from rest_framework import serializers
from .models import Item #Register
from .models import Register

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'username', 'password', 'created_at']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


# class RegistrationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Register
#         fields = ['username', 'password']