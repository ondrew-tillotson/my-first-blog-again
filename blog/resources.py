from .models import Record
from import_export import fields, resources

class RecordResource(resources.ModelResource):
    first_name = fields.Field(column_name='First Name',attribute='first_name')
    last_name = fields.Field(column_name='Last Name',attribute='last_name')
    email = fields.Field(column_name='Email Addy',attribute='email')
    phone = fields.Field(column_name='Phone Number',attribute='phone')
    address = fields.Field(column_name='=Street Addy',attribute='address')
    city = fields.Field(column_name='City',attribute='city')
    state = fields.Field(column_name='State',attribute='state')
    zipcode = fields.Field(column_name='Zipcode',attribute='zipcode')

    class Meta:
        model = Record
        fields = ('first_name','last_name','email','phone','address','city','state','zipcode')
        export_order = ('first_name','last_name','email','phone','address','city','state','zipcode')