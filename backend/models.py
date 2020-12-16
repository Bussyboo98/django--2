from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    name = models.CharField(max_length=150)
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Description')
    profile = models.FileField(null=True, blank=True, upload_to='uploads/')
    def __str__(self):
            return self.name
            
    def __str__(self):
        return self.cat_name
    
    class Meta():
        verbose_name_plural = 'Category'

    def profile_img(self):
          if self.profile:
              return self.profile.url
            
