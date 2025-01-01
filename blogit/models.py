from django.db import models

# Create your models here.
from django.db import models

class BlogDetails(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.CharField(max_length=100)
    blog_content = models.TextField()

    

