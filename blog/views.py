from django.shortcuts import render
from django.utils import timezone

from .models import *

# Create your views here.
def index(request):
  return render(request, 'blog/index.html', {'posts': Post.objects.filter(published_at__lte=timezone.now())})