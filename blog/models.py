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
<<<<<<< HEAD
#hiiiiiiii
=======
class CSVFile(models.Model):
        file = models.FileField(upload_to='csv_uploads/')
        uploaded_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.file.name
>>>>>>> bb7d07fcd490eb146dca1abcaa6dbf21c351e570
# Create your models here.
