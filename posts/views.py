import random

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from .forms import CreatePostForm, CreateCommentForm
from users.models import UserInfo, SystemUser


def not_admin_check(user):
    return not user.username == 'admin'


def can_post_check(user):
    user_info = get_object_or_404(UserInfo, pk=user.id)
    if user_info.posts_available() <= 1:
        return True
    else:
        return False


# def can_comment_check(user, post_id):
#     current_user = user.username
#     user_info = get_object_or_404(UserInfo, user_reference=current_user.username)
#     current_post = get_object_or_404(Post, pk=post_id)
#     if user_info.random_post == current_post:
#         return True
#     else:
#         return False


def has_already_voted(current_post, current_user):
    if current_post.up_votes_list.filter(username=current_user.username).exists():
        return 1
    else:
        return 0


def has_already_down_voted(current_post, current_user):
    if current_post.down_votes_list.filter(username=current_user.username).exists():
        return 1
    else:
        return 0


def has_already_voted_comment(current_comment, current_user):
    if current_comment.up_votes_list.filter(username=current_user.username).exists():
        return 1
    else:
        return 0


def has_already_down_voted_comment(current_comment, current_user):
    if current_comment.down_votes_list.filter(username=current_user.username).exists():
        return 1
    else:
        return 0


def index(request):
    latest_posts_list = Post.objects.order_by('-pub_date')[:30]     # TODO: Pagination
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return render(request, 'index.html', context)


def popular(request):
    # popular_posts_list = Post.objects.order_by('vote_difference')[:30]  # Cannot sort by model methods
    posts_list = Post.objects.all()
    popular_posts_list = sorted(posts_list, key=lambda votes: -(votes.up_votes_list.count()))[:30]
    # popular_posts_list = Post.objects.all()[:10]
    context = {
        'popular_posts_list': popular_posts_list,
    }
    return render(request, 'index.html', context)


def post(request, post_id):
    return HttpResponse("You're looking at the post with id %i" % post_id)


def detail(request, post_id):
    current_post = get_object_or_404(Post, pk=post_id)
    current_user = request.user
    has_voted = has_already_voted(current_post, current_user)
    has_down_voted = has_already_down_voted(current_post, current_user)
    return render(request, 'detail.html',
                  {'post': current_post, 'has_voted': has_voted, 'has_down_voted': has_down_voted})


@login_required
@user_passes_test(not_admin_check, login_url='/ADMINS_CANT_CREATE_POSTS/')  # TODO: Improve forwarding
@user_passes_test(can_post_check, login_url='/NOT_ENOUGH_XP/')  # TODO: Improve forwarding
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            p = Post(creator=current_user, post_title=form.cleaned_data['post_title'],
                     post_text=form.cleaned_data['post_text'], pub_date=timezone.now())
            p.save()
            user_info = get_object_or_404(UserInfo, user_reference=current_user)
            user_info.post_count += 1
            user_info.save()
            return redirect('posts:detail', p.id)
    else:
        form = CreatePostForm()
    return render(request, 'createPost.html', {'form': form})


@login_required
def vote(request, post_id, is_down_vote=0):
    current_post = get_object_or_404(Post, pk=post_id)
    current_user = request.user
    post_creator = get_object_or_404(SystemUser, id=current_post.creator.id)
    creator_info = get_object_or_404(UserInfo, user_reference=post_creator.id)
    has_already_voted_check = has_already_voted(current_post, current_user)
    has_already_down_voted_check = has_already_down_voted(current_post, current_user)
    if not is_down_vote:
        if not has_already_voted_check:
            if has_already_down_voted_check:
                current_post.down_votes_list.remove(current_user)
                creator_info.xp += 5
            current_post.up_votes_list.add(current_user)
            creator_info.xp += 5
        else:
            current_post.up_votes_list.remove(current_user)
            creator_info.xp -= 5
    else:
        if not has_already_down_voted_check:
            if has_already_voted_check:
                current_post.up_votes_list.remove(current_user)
                creator_info.xp -= 5
            current_post.down_votes_list.add(current_user)
            creator_info.xp -= 5
        else:
            current_post.down_votes_list.remove(current_user)
            creator_info.xp += 5
    creator_info.save()
    return redirect('posts:detail', current_post.id)


@login_required
def down_vote(request, post_id):
    is_down_vote = 1
    return redirect('posts:vote', post_id, is_down_vote)


@login_required
def vote_comment(request, comment_id, is_down_vote):
    current_comment = get_object_or_404(Comment, pk=comment_id)
    current_post = get_object_or_404(Post, pk=current_comment.post.id)
    current_user = request.user
    comment_creator = get_object_or_404(SystemUser, id=current_comment.creator.id)
    creator_info = get_object_or_404(UserInfo, user_reference=comment_creator.id)
    has_already_voted_check = has_already_voted_comment(current_comment, current_user)
    has_already_down_voted_check = has_already_down_voted_comment(current_comment, current_user)
    if not is_down_vote:
        if not has_already_voted_check:
            if has_already_down_voted_check:
                current_comment.down_votes_list.remove(current_user)
                creator_info.xp += 5
            current_comment.up_votes_list.add(current_user)
            creator_info.xp += 5
        else:
            current_comment.up_votes_list.remove(current_user)
            creator_info.xp -= 5
    else:
        if not has_already_down_voted_check:
            if has_already_voted_check:
                current_comment.up_votes_list.remove(current_user)
                creator_info.xp -= 5
            current_comment.down_votes_list.add(current_user)
            creator_info.xp -= 5
        else:
            current_comment.down_votes_list.remove(current_user)
            creator_info.xp += 5
    creator_info.save()
    return redirect('posts:detail', current_post.id)


@login_required
# @user_passes_test(can_comment_check(post_id), login_url='YOU_CANT_COMMENT_ON_THIS_POST')
def create_comment(request, post_id):  # Create permissions
    current_post = get_object_or_404(Post, pk=post_id)
    current_user = request.user
    user_info = get_object_or_404(UserInfo, user_reference=current_user.id)
    if user_info.random_post == current_post:
        if request.method == 'POST':
            form = CreateCommentForm(request.POST)
            if form.is_valid():
                comment = Comment(post=current_post, creator=current_user,
                                  comment_text=form.cleaned_data['comment_text'],
                                  pub_date=timezone.now())
                comment.save()
                user_info.random_post = None
                user_info.xp += 20
                user_info.save()
                return redirect('posts:detail', current_post.id)
        else:
            form = CreateCommentForm()
        return render(request, 'createComment.html', {'form': form, 'post': current_post})
    else:
        return HttpResponse("You are not allowed to comment on this post.")  # TODO: Proper ERROR page!


def random_comment(request):
    current_user = request.user
    user_info = get_object_or_404(UserInfo, user_reference=current_user.id)
    if user_info.random_post is None:
        all_posts = Post.objects.all()
        random_post = random.choice(all_posts)
        random_id = random_post.id
        user_info.random_post = random_post
        user_info.save()
        return redirect('posts:detail', random_id)
    else:
        return redirect('posts:detail', user_info.random_post.id)


def search(request):
    query = request.GET['search_term']
    search_posts_list = Post.objects.filter(post_title__contains=query)
    context = {
        'search_posts_list': search_posts_list,
    }
    return render(request, 'index.html', context)
