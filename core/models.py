from django.db import models

# Create your models here.


class  Licenses(models.Model):
    type = models.CharField(max_length=255,blank=True,null=True)
    number = models.CharField(max_length=255,blank=True,null=True)
    code = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)    
    core_id = models.CharField(max_length=255,blank=True,null=True)
    name =  models.CharField(max_length=255,blank=True,null=True)
    grant_date = models.CharField(max_length=255,blank=True,null=True)
    expiry_date =  models.CharField(max_length=255,blank=True,null=True)
    holder=  models.CharField(max_length=255,blank=True,null=True)
    cadastral_unit = models.CharField(max_length=255,blank=True,null=True)