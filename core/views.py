from django.shortcuts import render
from .models import *

# Create your views here.
def dashboard(request):
    results = Licenses.objects.all().order_by('id')
    blocked = blockedLicenses.objects.all().count()
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    context = {        
        'licenses':results,
        'total_licenses':results.count(),
        'blocked':blocked,
        'registed':registed,
        'pending':pending
    }
    return render(request,'core/dashboard.html',context)


def blocked_licenses_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')   
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    context = {        
        'licenses':results,
        'total_licenses':results1.count(),
        'blocked':results.count(),        
        'registed':registed,
        'pending':pending
    }
    return render(request,'core/block.html',context)


def registed_measures_view(request):    
    results1 = Licenses.objects.all().order_by('id')
    measures = registered_measures.objects.all()
    blocked_licenses = blockedLicenses.objects.all()
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    context = {        
        'measures':measures,
        'total_licenses':results1.count(),
        'blocked':blocked_licenses.count(),                
        'registed':registed,
        'pending':pending
    }
    return render(request,'core/registed_measure.html',context)


def last_month_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = lastMonthLicenses.objects.all()
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'blocked':results.count(),
        'registed':registed,
        'pending':pending
    }
    return render(request,'core/lastmonth.html',context)



def pending_measures_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = pendingMeasures.objects.all()
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'blocked':results.count(),
        'registed':registed,
        'pending':pending
    }
    return render(request,'core/pending_measure.html',context)



def pending_application_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = pendingApplications.objects.all()
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'blocked':results.count(),
        'recent':lastmonthLicenses.count(),
        'registed':registed,
        'pending':pending
    }
    return render(request,'core/pen-app.html',context)



def register_application_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = registeredApplications.objects.all()
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'blocked':results.count(),
        'recent':lastmonthLicenses.count(),
        'registed':registed,
        'pending':pending
    }
    return render(request,'core/reg-app.html',context)