from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import *
from .forms import *

# Create your views here.
def index(request):
  return render(request, 'blog/index.html', {'posts': Post.objects.filter(published_at__lte=timezone.now())})

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)

  if request.user.is_active:
    if request.method == 'POST':
      comment_form = CommetForm(request.POST)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.creator = request.user
        comment.content_object = post
        comment.save()
        return redirect(request.path_info) 
    else:
      comment_form = CommetForm()
  else:
    comment_form = None

  return render(request, 'blog/post-detail.html', {'post': post, 'comment_form': comment_form})