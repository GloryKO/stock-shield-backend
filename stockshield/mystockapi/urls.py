from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import InventoryViewSet,UserViewSet#RegistrationViewSet

router = SimpleRouter()
router.register('users',UserViewSet),
router.register('',InventoryViewSet),
#router.register('register',RegistrationViewSet)
urlpatterns = router.urls