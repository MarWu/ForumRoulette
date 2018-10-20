import datetime

from django.db import models
from users import models as userInfo
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    post_title = models.CharField(max_length=200)
    post_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

    def time_since_published(self):
        return timezone.now() - self.pub_date


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
