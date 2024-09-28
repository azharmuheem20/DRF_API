# myapp/serializers.py

from rest_framework import serializers  # Import the serializers module
from .models import Category, SubCategory  # Import your models

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory  # Specify the model to serialize
        fields = ['id', 'name', 'category']  # Specify the fields to include in the serialization

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)  # Nested serializer for related subcategories

    class Meta:
        model = Category  # Specify the model to serialize
        fields = ['id', 'name', 'subcategories']  # Specify the fields to include in the serialization
