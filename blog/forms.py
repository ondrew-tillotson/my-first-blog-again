from django import forms

from .models import Post,Record
from .models import CSVFile


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class UploadFileForm(forms.Form):
    csv_file = forms.FileField()



# FORMAT_CHOICES 

class NewForm(forms.Form):
    options = (
        ('csv', 'csv'),
        ('xls', 'xls'),
    )
    
    category = forms.CharField(widget=forms.Select(choices=options), label='Export To:')
