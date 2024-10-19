from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)  # Register the OrderViewSet with the router

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
