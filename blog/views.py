from django.shortcuts import redirect
import pandas as pd

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

import io
# Create your views here.

from .models import Post # Assuming you have a Post model
from .models import CSVFile

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from .models import Post # Assuming you have a Post model
from .forms import PostForm
from .forms import UploadFileForm

def home_page(request):
	return render(request,'blog/base.html',{})

#def post_list(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#return render(request, 'blog/post_list.html', {'posts': posts})







#posts=	Post.objects.get(pk=pk)

 # posts = Post.objects.all() # Fetch all posts from the database


def upload_csv(request, *args):
	print(args)
	#args returns () but why
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
    # Read the file into a DataFrame
		decoded_file = request.read().decode('utf-8')
		#print(decoded_file)
		df = pd.read_csv(io.StringIO(decoded_file))
		#print(df)
	    # Rename columns based on the user-defined mapping
		df.rename(columns=args, inplace=True)

	    # Create model instances and use bulk_create for efficiency
		instances = [
			CSVFile(**row) for row in df.to_dict(orient='records')
		]
		CSVFile.objects.bulk_create(instances)
	else:
		form = UploadFileForm()
	return render(request, 'upload_csv.html', {'form': form})
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






