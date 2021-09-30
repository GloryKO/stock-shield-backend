from rest_framework  import viewsets
from .models import Inventory
from .serializers import InventorySerializers
from .permissions import IsAuthorOrReadOnly

class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthorOrReadOnly,)
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializers


