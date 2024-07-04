from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def new_post(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'blog/new_post.html')