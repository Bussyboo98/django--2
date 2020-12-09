from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    age = models.PositiveIntegerField()
    website = models.URLField(blank=True, null=True)

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.cat_name


class Post(models.Model):
    pst_title = models.CharField(max_length=150)
    pst_image = models.FileField(null=True, blank=True, upload_to='uploads/')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_id = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)