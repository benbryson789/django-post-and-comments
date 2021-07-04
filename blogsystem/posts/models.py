from django.db import models

# Create your models here.

class Posts(models.Model):
    title =  models.CharField(max_length=255)
    content = models.TextField()

class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    comment_title=models.CharField(max_length=255)
    comment_content=models.TextField()
    post_id =models.IntegerField()
