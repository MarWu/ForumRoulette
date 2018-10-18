from django.db import models


class User(models.Model):   # TestUser: Test | TestPassword123
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = 'How do I do this?!?'
    create_date = models.DateTimeField('date created')
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username
