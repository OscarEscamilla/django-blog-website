from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/blog_images/') 
    body = models.TextField()
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(default=datetime.date.today) 
