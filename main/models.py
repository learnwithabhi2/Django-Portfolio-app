from django.db import models

# Create your models here.


class UserImage(models.Model):
    photo = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
