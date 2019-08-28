from django.db import models
class csv_table(models.Model):
    csv_id = models.AutoField(primary_key=True)
    inventory_key= models.IntegerField()
    catalog_no= models.CharField(max_length=50)
    catalog_colour= models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    catalog_price = models.CharField(max_length=50)
    is_on_sale = models.CharField(max_length=50)
class csvfiles(models.Model):
    csv_files_id = models.AutoField(primary_key=True)
    name = models.FileField(upload_to = 'media/uploads',null=True)
    date_created = models.DateTimeField()