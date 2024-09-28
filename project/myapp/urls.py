# myapp/urls.py

from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView, SubCategoryListCreateView, SubCategoryDetailView, DeleteAllCategoriesView, DeleteAllSubCategoriesView
from .views import ProtectedView , RegisterUserView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('categories/delete-all/', DeleteAllCategoriesView.as_view(), name='delete-all-categories'),
    path('subcategories/delete-all/', DeleteAllSubCategoriesView.as_view(), name='delete-all-subcategories'),
    path('protected/', ProtectedView.as_view(), name='protected_view'),
    path('register/', RegisterUserView.as_view(), name='register'),
]
