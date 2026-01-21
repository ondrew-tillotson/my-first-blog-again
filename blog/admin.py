from django.contrib import admin

# Register your models here.
from .models import CSVFile
#For downloading csv button
from .models import Record
from import_export import resources
from import_export.admin import ExportActionMixin, ImportExportActionModelAdmin
from import_export.fields import Field


class RecordResource(resources.ModelResource):

    class Meta:
        model = Record
        fields = ('first_name','last_name','email','phone','address','city','state','zipcode')
        export_order = ('first_name','last_name','email','phone','address','city','state','zipcode')
    

admin.site.register([CSVFile,Record])

