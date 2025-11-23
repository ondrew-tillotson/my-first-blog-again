from django.shortcuts import redirect
<<<<<<< HEAD

from django.shortcuts import render, get_object_or_404
from django.utils import timezone


# Create your views here.

from .models import Post # Assuming you have a Post model

=======
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from .models import Post # Assuming you have a Post model
>>>>>>> bb7d07fcd490eb146dca1abcaa6dbf21c351e570
from .forms import PostForm


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	#posts=	Post.objects.get(pk=pk)

 # posts = Post.objects.all() # Fetch all posts from the database
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)

	#posts=	Post.objects.get(pk=pk)

 # posts = Post.objects.all() # Fetch all posts from the database
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)


	else:
		form = PostForm()

    #form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
<<<<<<< HEAD
# Create your views here.
=======
# Create your views here.
>>>>>>> bb7d07fcd490eb146dca1abcaa6dbf21c351e570
