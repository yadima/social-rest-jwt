from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.title