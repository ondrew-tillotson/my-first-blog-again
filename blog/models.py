
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
#hiiiiiiii
class CSVFile(models.Model):
        file = models.FileField(upload_to='csv_uploads/')
        uploaded_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.file.name
        def upload(self):
            self.save()

# Create your models here.

# HELLLO THIS IS the model for FOR THE CSV DOWNLOAD

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return(f"{self.first_name}")

class MiniRecord(models.Model):
    #uploaded_at = models.DateTimeField(auto_now_add=True)

    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    class Meta:
        ordering = ['fname']

    def __str__(self):
        return(f"{self.fname}")
