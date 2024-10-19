# products/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Create user with hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']
def validate(self, data):
        if data.get('price') is None or data.get('price') <= 0:
            raise serializers.ValidationError({"price": "Price must be a positive number."})
        
        if not data.get('name'):
            raise serializers.ValidationError({"name": "Name is required."})
        
        if data.get('stock_quantity') is None or data.get('stock_quantity') < 0:
            raise serializers.ValidationError({"stock_quantity": "Stock Quantity cannot be negative."})
        
        return data