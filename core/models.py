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

    def __str__(self):
        return self.code



class  blockedLicenses(models.Model):
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

    def __str__(self):
        return self.code


class  lastMonthLicenses(models.Model):
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

    def __str__(self):
        return self.code



class registeredApplications(models.Model):	
    number = models.CharField(max_length=255,blank=True,null=True) 
    code = models.CharField(max_length=255,blank=True,null=True)        
    type = models.CharField(max_length=255,blank=True,null=True)        
    minerals = models.CharField(max_length=255,blank=True,null=True)      
    registration_date = models.CharField(max_length=255,blank=True,null=True)        
    status = models.CharField(max_length=255,blank=True,null=True)        
    applicant = models.CharField(max_length=255,blank=True,null=True)        
    area = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.code
    

class pendingApplications(models.Model):	
    number = models.CharField(max_length=255,blank=True,null=True) 
    code = models.CharField(max_length=255,blank=True,null=True)        
    type = models.CharField(max_length=255,blank=True,null=True)      
    registration_date = models.CharField(max_length=255,blank=True,null=True)        
    status = models.CharField(max_length=255,blank=True,null=True)        
    name= models.CharField(max_length=255,blank=True,null=True)        
    area = models.CharField(max_length=255,blank=True,null=True)
    applicant = models.CharField(max_length=255,blank=True,null=True)
    minerals = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.code
        

class registered_measures(models.Model):
    number = models.CharField(max_length=255,blank=True,null=True)	 
    code = models.CharField(max_length=255,blank=True,null=True)        
    name = models.CharField(max_length=255,blank=True,null=True)        
    type = models.CharField(max_length=255,blank=True,null=True)        
    registration_date = models.CharField(max_length=255,blank=True,null=True)        
    status = models.CharField(max_length=255,blank=True,null=True)        
    area = models.CharField(max_length=255,blank=True,null=True)        
    def __str__(self):
        return self.code
    

class pendingMeasures(models.Model):
    number = models.CharField(max_length=255,blank=True,null=True)	 
    code = models.CharField(max_length=255,blank=True,null=True)        
    name = models.CharField(max_length=255,blank=True,null=True)        
    type = models.CharField(max_length=255,blank=True,null=True)        
    registration_date = models.CharField(max_length=255,blank=True,null=True)        
    status = models.CharField(max_length=255,blank=True,null=True)        
    area = models.CharField(max_length=255,blank=True,null=True)  
    minerals  = models.CharField(max_length=255,blank=True,null=True)  
    applicant = models.CharField(max_length=255,blank=True,null=True)  
    def __str__(self):
        return self.code
    


class YearlyCount(models.Model):

    year = models.CharField(max_length=255,blank=True,null=True)
    total = models.CharField(max_length=255,blank=True,null=True)
	 
    def __str__(self):
        return self.code


class RestrictedAreas(models.Model):

    number = models.CharField(max_length=255,blank=True,null=True)
    code = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    type = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255,blank=True,null=True)
    enacted_by= models.CharField(max_length=255,blank=True,null=True)
    decree_number=models.CharField(max_length=255,blank=True,null=True)
    area = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.code


class Coordinates(models.Model):
    code = models.CharField(max_length=255,blank=True,null=True)
    longitude = models.CharField(max_length=255,blank=True,null=True)
    latitude = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.code