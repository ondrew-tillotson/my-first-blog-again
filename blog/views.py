from django.shortcuts import render
from .models import Post # Assuming you have a Post model
def post_list(request):
  posts = Post.objects.all() # Fetch all posts from the database
  return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.
