# myapp/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny



class RegisterUserView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

# View for Category List and Create
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# View for Category Retrieve, Update, Delete
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# View for SubCategory List and Create
class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

# View for SubCategory Retrieve, Update, Delete
class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

# View to delete all categories and subcategories
class DeleteAllCategoriesView(APIView):
    def delete(self, request, *args, **kwargs):
        # Delete all categories, cascading delete for subcategories
        Category.objects.all().delete()
        return Response({"message": "All categories and subcategories have been deleted."}, status=status.HTTP_204_NO_CONTENT)

# View to delete all subcategories only
class DeleteAllSubCategoriesView(APIView):
    def delete(self, request, *args, **kwargs):
        # Delete all subcategories without affecting categories
        SubCategory.objects.all().delete()
        return Response({"message": "All subcategories have been deleted."}, status=status.HTTP_204_NO_CONTENT)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        return Response({"message": "Hello, you are authenticated!"})    
