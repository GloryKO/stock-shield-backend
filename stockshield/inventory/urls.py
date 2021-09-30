from django.db import router
from rest_framework.routers import SimpleRouter
from .views import InventoryViewSet

router = SimpleRouter()

router.register('inventory',InventoryViewSet),

urlpatterns = router.urls