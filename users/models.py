from django.contrib.auth.models import User as SystemUser
from django.db import models
from posts.models import Post


# class User(models.Model):   # TestUser: Test | TestPassword123
#     username = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = 'How do I do this?!?'
#     create_date = models.DateTimeField('date created')
#     post_count = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.username


class UserInfo(models.Model):
    user_reference = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    post_count = models.IntegerField(default=0)
    random_post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.DO_NOTHING)   # TODO: User XP

    def __str__(self):
        return self.user_reference.username
