from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register([Coordinates,RestrictedAreas,YearlyCount,pendingMeasures,registered_measures,pendingApplications,registeredApplications,lastMonthLicenses,blockedLicenses,Licenses])
