from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import CreatePostForm


def index(request):
    latest_posts_list = Post.objects.order_by('-pub_date')[:10]
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return render(request, 'index.html', context)


def post(request, post_id):
    return HttpResponse("You're looking at the post with id %i" % post_id)


def detail(request, post_id):
    current_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': current_post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            p = Post(creator=request.user, post_title=form.cleaned_data['post_title'], post_text=form.cleaned_data['post_text'], pub_date=timezone.now())
            p.save()
            return redirect('posts:index')
    else:
        form = CreatePostForm()
    return render(request, 'createPost.html', {'form': form})
