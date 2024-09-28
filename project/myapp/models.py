from django.db import models

# Create your models here.
from django.db import models
from django.db.models import F, Func
from django.db.models.functions import Cast
from django.db.models import IntegerField

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('property', 'Property'),
        ('jewelry', 'Jewelry'),
        ('cars', 'Cars'),
    ]
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f'{self.name} ({self.category.get_name_display()})'
