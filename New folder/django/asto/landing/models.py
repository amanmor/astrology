from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    image=models.ImageField()
    info=RichTextField()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('gemstone', 'Gemstone'),
        ('rudraksh', 'Rudraksh'),
        ('yantras','Yantras')
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name}({self.category})"