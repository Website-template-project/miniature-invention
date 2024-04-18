from rest_framework import status,viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import ProductPortfolio
from .serializers import ProductSerializer,UserSerializer
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

"""
    View to list all users in the system.
"""    
@api_view(['GET'])
def get_users(request):
    usernames = [user.username for user in User.objects.all()]
    return Response(usernames,status = status.HTTP_200_OK)   
@api_view(['GET'])
def get_product_portfolio(request):
    # ProductPortfolio.objects.create(title = "Simple project", status = "In Development", 
    #                                 description = "This is a very basics website")
    res = [{"title":i.title,"status":i.status,
            "description":i.description} for i in ProductPortfolio.objects.all()]  
    return Response(res,status = status.HTTP_200_OK)

"""
Create: POST
Read: GET
Update: PUT
Delete: DELETE
"""
@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_product(request):
    queryset = ProductPortfolio.objects.all()
    data = request.data
    d = {}
    for key in data:
        d[key] = data[key]
    data = d
    if(request.method == 'POST'):
        try:
            ProductPortfolio.objects.create(**data)
            return Response("Request successful",
                            status = status.HTTP_201_CREATED)
        except Exception as e:
            return Response("Request unsuccessful",
                            status = status.HTTP_400_BAD_REQUEST)
    elif(request.method == 'DELETE'):
        try:
            ProductPortfolio.objects.get(**data).delete()
            return Response("Request unsuccessful",
                            status = status.HTTP_200_OK)
        except Exception as e:
            return Response("Request unsuccessful",
                            status = status.HTTP_400_BAD_REQUEST)
    elif(request.method == 'GET'):
        pass
    elif(request.method == 'PUT'):
        pass
    return Response(str(data),status = status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

# class ListUsers(APIView):
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames,status = status.HTTP_200_OK)