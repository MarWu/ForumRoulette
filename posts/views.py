from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from .forms import CreatePostForm, CreateCommentForm
from users.models import UserInfo


def not_admin_check(user):
    return not user.username == 'admin'


def index(request):
    latest_posts_list = Post.objects.order_by('-pub_date')[:30]
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return render(request, 'index.html', context)


def post(request, post_id):
    return HttpResponse("You're looking at the post with id %i" % post_id)


def detail(request, post_id):
    current_post = get_object_or_404(Post, pk=post_id)
    current_user = request.user
    if current_post.up_votes_list.filter(username=current_user.username).exists():
        has_voted = 1
    else:
        has_voted = 0
    return render(request, 'detail.html', {'post': current_post, 'has_voted': has_voted})


@login_required
@user_passes_test(not_admin_check, login_url='/ADMINS_CANT_CREATE_POSTS/')
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            current_user = request.user
            p = Post(creator=current_user, post_title=form.cleaned_data['post_title'],
                     post_text=form.cleaned_data['post_text'], pub_date=timezone.now())
            p.save()
            post_count = get_object_or_404(UserInfo, user_reference=current_user)
            post_count.post_count += 1
            post_count.save()
            return redirect('posts:detail', p.id)
    else:
        form = CreatePostForm()
    return render(request, 'createPost.html', {'form': form})


@login_required
def vote(request, post_id):
    current_post = get_object_or_404(Post, pk=post_id)
    current_user = request.user
    current_post.up_votes_list.add(current_user)
    return redirect('posts:detail', current_post.id)


def create_comment(request, post_id):   # Create permissions
    current_post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            comment = Comment(post=current_post, creator=current_user, comment_text=form.cleaned_data['comment_text'],
                              pub_date=timezone.now())
            comment.save()
            return redirect('posts:detail', current_post.id)
    else:
        form = CreateCommentForm()
    return render(request, 'createComment.html', {'form': form, 'post': current_post})
