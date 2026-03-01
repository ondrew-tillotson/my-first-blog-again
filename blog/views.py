from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone

from .models import Post,CSVFile, Record,MiniRecord # Assuming you have a Post model
from .forms import PostForm, NewForm,UploadFileForm
from django.core.management import call_command



from django.views.generic import ListView, FormView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import context
from .resources import RecordResource
from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import io
import csv
import pandas as pd



#def home_page(request):
	#return render(request,'blog/base.html',{})




#Hannah: We need to give upload_csv a new dictionary "cleaning_methods" structured like
#"{'Dedupe': True, 'Caps names': False, 'Valid Address?':False}"
#and it will come from whatever ui we make that allows people to select how they want it to be cleaned

def upload_csv(request, *args):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        uploaded_file = request.FILES['csv_file']
        try:
            csv_data = uploaded_file.read().decode('utf-8')
            data_io = io.StringIO(csv_data)
            reader = csv.DictReader(data_io)

            objs = [MiniRecord(fname=row['fname'], lname=row['lname']) for row in reader]
            #print(MiniRecord.objects.bulk_create(objs))

            MiniRecord.objects.bulk_create(objs)
            queryset = MiniRecord.objects.all()
            #print(queryset)
            df = pd.read_csv(data_io)         
            #print(df)
			#and then we need to cycle through cleaning_methods and pass it to functions
			#so if 'Depupe' is True in our dictionary, we pass df to a dedupe(df) function.


			#and then, HANNAH, huge: we pass it off to download_csv, which we need to structure 
			#around a button that pops up after uploading the csv, which we'll need to make an html file
			#view, and url for it.  Also I believe a DownloadFileForm model in models.py
            #download_csv(df)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="{filename}.csv"'.format(filename='myname')
            writer = csv.writer(response)
            writer.writerow([column for column in df.columns])
            writer.writerows(df.values.tolist())
            #print(response)
            return render(response, 'download.html', {})
        except Exception as e:
            print(e)
            return render(request, 'download.html', {})
    else:
        form = UploadFileForm()

    return render(request, 'upload_csv.html', {'form': form})


def download_csv(df):
	print(df.head())




#Download csv from sqlite db

def RecordList(request):
    queryset = Record.objects.all()
    print(Record.objects.all())
    form = NewForm()
    context = {'obj': queryset, 'form':form}
    print(request.method)
    if request.method=='POST':
        form = NewForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            dataFormat = (form.cleaned_data['category'])


            # If User Selects CSV Format
            if dataFormat == 'csv':
                record_resource = RecordResource()
                dataset = record_resource.export()
                response = HttpResponse(dataset.csv, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="recordzz.csv"'
                return response

            # If User Selects XLS Format
            elif dataFormat == 'xls':
                record_resource = RecordResource()
                dataset = record_resource.export()
                response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="recordz.xls"'
                return response
        else:
            print('Form Is Invalid')
    else:
        form = NewForm()
    return render(request, 'download.html', context)


#Logging in users to access tool
def home(request):
    records = Record.objects.all()
    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('blog:home')
        else:
            messages.success(request, "There was an error :/ Try again")
            return redirect('blog:home')
    else:
        return render(request, 'home.html',{'records': records})