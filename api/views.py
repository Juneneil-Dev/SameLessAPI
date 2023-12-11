from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Item, Register
from .serializers import ItemSerializer, RegisterSerializer, LoginSerializer

class DumpItAPI(APIView):
    
    # def get(self,request):
    #     items = [
    #         "apple",
    #         "mango",
    #         "grapes"
    #     ]
    #     response_data = {"datas":items}
    #     return Response(response_data,status=status.HTTP_200_OK)

    # def post(self,request):
    #     response_data = {"response":"Hello Its Post method"}
    #     return Response(response_data,status=status.HTTP_200_OK)

    # def post(self,request):
    #     name = request.data.get('name')
    #     response_data = {"name": name}
    #     return Response(response_data,status=status.HTTP_200_OK)

    def get(self,request):
        items = Item.objects.all()
        items_data = ItemSerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def add_post(self,request):
        name = request.data.get('name')
        Item.objects.create(name=name)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        name = request.data.get('name')
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item doesnot exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.name = name
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    # def delete(self,request):
    #     id = request.data.get('id')
    #     item = Item.objects.filter(id=id).first()
    #     if item is None:
    #         response_data = {"response": "Item does not exists"}
    #         return Response(response_data,status=status.HTTP_404_NOT_FOUND)

    #     item.delete()
    #     response_data = {"response": "item Delete"}
    #     return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = Item.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)


    # def registration(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
        
    #     response = Register.register_user(username, password)
    #     return response

    def reg_post(self, request):
        # Get data from the request
        data = request.data

        # Validate the data using the serializer
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            # Create a new user
            Register.objects.create(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            
            response_data = {"response": "User registered successfully"}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        # Get data from the request
        data = request.data

        # Validate the data using the serializer
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            # Authenticate user
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Check if the user exists
            try:
                user = Register.objects.get(username=username, password=password)
            except Register.DoesNotExist:
                response_data = {"response": "Invalid credentials"}
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

            response_data = {"response": "Login successful", "user_id": user.id}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
