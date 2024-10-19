# products/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from django.http import HttpResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter  # Correct import for SearchFilter
from django.db.models import Q

# User ViewSet for managing users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Homepage view
def homepage(request):
    return HttpResponse("<h1>Welcome to the E-commerce API</h1><p>Use the /api/ endpoints for the API.</p>")

# Custom pagination class
class ProductPagination(PageNumberPagination):
    page_size = 10  # Default number of products per page
    page_size_query_param = 'page_size'  # Allow clients to set page size
    max_page_size = 100  # Maximum page size allowed

# Product ViewSet for managing products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ProductPagination  # Use custom pagination
    
    # Enable filtering
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)  # Fixed import here
    search_fields = ['name', 'category__name']  # Allow search on product name and category name
    filterset_fields = {
        'category': ['exact'],  # Filter by category
        'price': ['lt', 'gt'],  # Filter by price range (less than, greater than)
        'stock_quantity': ['gt'],  # Filter by stock quantity available
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(Q(name__icontains=search))  # Case-insensitive partial match on product name
        return queryset
