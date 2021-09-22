from django.contrib.auth import get_user_model
from django.db.models import query
from django.shortcuts import render
from rest_framework  import viewsets
from .models import CustomUser, Product_Inventory
from .serializers import InventorySerializers,UserSerializer#UserRegistrationSerializer
from .permissions import IsAuthorOrReadOnly

class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthorOrReadOnly,)
    queryset = Product_Inventory.objects.all()
    serializer_class = InventorySerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
'''
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset =CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    '''