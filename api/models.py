from django.db import models

# Create your models here.

class Item(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)

class Register(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    # @classmethod
    # def register_user(cls, username, password):
    #     # Validate username and password
    #     if not username or not password:
    #         response_data = {"response": "Username and password are required"}
    #         return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    #     # Check if the username already exists
    #     if cls.objects.filter(username=username).exists():
    #         response_data = {"response": "Username already exists"}
    #         return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    #     # Create a new user
    #     cls.objects.create(username=username, password=password)

    #     response_data = {"response": "User registered successfully"}
    #     return Response(response_data, status=status.HTTP_201_CREATED)
