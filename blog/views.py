from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import *

# Create your views here.
def index(request):
  return render(request, 'blog/index.html', {'posts': Post.objects.filter(published_at__lte=timezone.now())})

def post_detail(request, slug):
  return render(request, 'blog/post-detail.html', {'post': get_object_or_404(Post, slug=slug)})