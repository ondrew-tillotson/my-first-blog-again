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




#Hannah: We need to give upload_csv a new dictionary "cleaning_methods" structured like
#"{'Dedupe': True, 'Caps names': False, 'Valid Address?':False}"
#and it will come from whatever ui we make that allows people to select how they want it to be cleaned

def upload_csv(request, *args):
	if request.method == 'POST' and request.FILES.get('csv_file'):
		uploaded_file = request.FILES['csv_file']
		try:
			csv_data = uploaded_file.read().decode('utf-8')
			data_io = io.StringIO(csv_data)
			df = pd.read_csv(data_io)

            
           
			#and then we need to cycle through cleaning_methods and pass it to functions
			#so if 'Depupe' is True in our dictionary, we pass df to a dedupe(df) function.


			#and then, HANNAH, huge: we pass it off to download_csv, which we need to structure 
			#around a button that pops up after uploading the csv, which we'll need to make an html file
			#view, and url for it.  Also I believe a DownloadFileForm model in models.py

			download_csv(df)

			return render(request, 'upload_csv.html', {})

		except Exception as e:
			return render(request, 'upload_csv.html', {})
	else:
		form = UploadFileForm()
	return render(request, 'upload_csv.html', {'form': form})

def download_csv(df):
	print(df.head())






