from django.utils import timezone

from django.test import TestCase
from posts.models import Post
from django.contrib.auth.models import User


class PostVoteTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='TestUser1')
        user2 = User.objects.create(username='TestUser2')
        post = Post.objects.create(creator=user1, post_title='TestTitle1', post_text='Test1', pub_date=timezone.now())
        user1.save()
        user2.save()
        post.save()

    def test_no_vote(self):
        post = Post.objects.get(post_title='TestTitle1')
        self.assertEqual(post.up_vote_count(), 0)

    def test_vote(self):
        post = Post.objects.get(post_title='TestTitle1')
        user1 = User.objects.get(username='TestUser1')
        post.up_votes_list.add(user1)
        self.assertEqual(post.up_vote_count(), 1)
