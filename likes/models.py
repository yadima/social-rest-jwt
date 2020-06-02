from django.conf import settings
from django.db import models
from posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        default_related_name = 'post'
        unique_together = ('post', 'user')

    def __str__(self):
        return f'post: {self.post.id} - user: {self.user}'
