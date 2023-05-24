from datetime import datetime, date

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.TextField(max_length=500)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    post_file = models.FileField(upload_to="files/", null=True, blank=True)
    post_created = models.DateTimeField(default=datetime.now())
    post_edited = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.post_title


class BlockedPostUsers(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Blocked"


class PostComment(models.Model):
    comment_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_content = models.TextField(max_length=100)
    comment_timestamp = models.DateTimeField(default=datetime.now())
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return "'" + Post.objects.filter(id=self.comment_post_id.id).values('post_title').get()['post_title'] + "' Post Comment"

