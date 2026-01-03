from django import forms

from .models import Post
from .models import CSVFile


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class UploadFileForm(forms.Form):
    csv_file = forms.FileField()
