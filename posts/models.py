import datetime
import random
from random import randint

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    post_title = models.CharField(max_length=200)
    post_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    # up_votes = models.IntegerField(default=0)
    # down_votes = models.IntegerField(default=0)
    up_votes_list = models.ManyToManyField(User, related_name='vote_list', blank=True)
    down_votes_list = models.ManyToManyField(User, related_name='down_votes_list', blank=True)

    def __str__(self):
        return self.post_title

    def time_since_published(self):
        return timezone.now() - self.pub_date

    def up_vote_count(self):
        return self.up_votes_list.count()

    def down_vote_count(self):
        return self.down_votes_list.count()

    def pub_date_printable(self):
        if timezone.now().year - self.pub_date.year > 0:
            return "over " + str(timezone.now().year - self.pub_date.year) + " year(s) ago"
        if timezone.now().month - self.pub_date.month > 0:
            return "over " + str(timezone.now().month - self.pub_date.month) + " month(s) ago"
        if timezone.now().day - self.pub_date.day > 6:
            return str(int(timezone.now().day - self.pub_date.day / 7)) + " week(s) ago"
        if timezone.now().day - self.pub_date.day > 0:
            return str(timezone.now().day - self.pub_date.day) + " day(s) ago"
        if timezone.now().hour - self.pub_date.hour > 0:
            return str(timezone.now().hour - self.pub_date.hour) + " hour(s) ago"
        if timezone.now().minute - self.pub_date.minute > 0:
            return str(timezone.now().minute - self.pub_date.minute) + " minute(s) ago"
        else:
            return "just now"

    # def random(self):
    #     all_posts = self.id.
    #     return random.choice(all_posts)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    # up_votes = models.IntegerField(default=0)
    # down_votes = models.IntegerField(default=0)
    up_votes_list = models.ManyToManyField(User, related_name='comment_vote_list', blank=True)
    down_votes_list = models.ManyToManyField(User, related_name='comment_down_vote_list', blank=True)

    def __str__(self):
        return self.comment_text

    def up_vote_count(self):
        return self.up_votes_list.count()

    def down_vote_count(self):
        return self.down_votes_list.count()

    def pub_date_printable(self):
        if timezone.now().year - self.pub_date.year > 0:
            return "over " + str(timezone.now().year - self.pub_date.year) + " year(s) ago"
        if timezone.now().month - self.pub_date.month > 0:
            return "over " + str(timezone.now().month - self.pub_date.month) + " month(s) ago"
        if timezone.now().day - self.pub_date.day > 6:
            return str(int(timezone.now().day - self.pub_date.day / 7)) + " week(s) ago"
        if timezone.now().day - self.pub_date.day > 0:
            return str(timezone.now().day - self.pub_date.day) + " day(s) ago"
        if timezone.now().hour - self.pub_date.hour > 0:
            return str(timezone.now().hour - self.pub_date.hour) + " hour(s) ago"
        if timezone.now().minute - self.pub_date.minute > 0:
            return str(timezone.now().minute - self.pub_date.minute) + " minute(s) ago"
        else:
            return "just now"
