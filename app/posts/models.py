from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
