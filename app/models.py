from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from .managers import Itemmanager
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user','price'])
        ]

    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True, related_name='category')
    product = models.CharField(max_length=50, db_index=True)
    description= models.TextField(max_length=200)
    price=models.IntegerField(db_index=True)
    image = models.ImageField(upload_to='product_image',default='itemimage.jpg',null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return f"{self.product} -- {self.price}"
    
    def get_absolute_url(self):
        return reverse('app:home')
    



class Login(models.Model):
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    

    def __str__(self):
        return self.username