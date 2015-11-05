from django.db import models

# Create your models here.
class Search_data(models.Model):
    monitor_name = models.CharField(max_length=50)
    index = models.CharField(max_length=50)
    query = models.CharField(max_length=50, null=True)
    fields = models.CharField(max_length=500, null=True)
    field = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    size = models.IntegerField(null=True)
    sub_fields = models.CharField(max_length=500, null=True)
    mothod_type = models.CharField(max_length=20, null=True)
    pic_type = models.CharField(max_length=20, null=True)
    num_dashboard = models.CharField(max_length=2, null=True)
