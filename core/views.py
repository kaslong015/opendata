from django.shortcuts import render
from .models import *

# Create your views here.
def dashboard(request):
    results = Licenses.objects.all().order_by('id')
    context = {        
        'licenses':results,
        'total_licenses':results.count(),
    }
    return render(request,'core/dashboard.html',context)


def blocked_licenses_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    context = {        
        'licenses':results,
        'total_licenses':results1.count(),
        'total_blocked_licenses':results.count(),
    }
    return render(request,'core/block.html',context)


def registed_measures_view(request):    
    results1 = Licenses.objects.all().order_by('id')
    measures = registered_measures.objects.all()
    blocked_licenses = blockedLicenses.objects.all()
    context = {        
        'measures':measures,
        'total_licenses':results1.count(),
        'total_blocked_licenses':blocked_licenses.count(),
    }
    return render(request,'core/registed_measure.html',context)


def last_month_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = lastMonthLicenses.objects.all()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'total_blocked_licenses':results.count(),
    }
    return render(request,'core/lastmonth.html',context)



def pending_measures_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = pendingMeasures.objects.all()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'total_blocked_licenses':results.count(),
    }
    return render(request,'core/pending_measure.html',context)



def pending_application_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = pendingApplications.objects.all()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'total_blocked_licenses':results.count(),
    }
    return render(request,'core/pen-app.html',context)



def register_application_view(request):
    results = blockedLicenses.objects.all()
    results1 = Licenses.objects.all().order_by('id')
    lastmonthLicenses = registeredApplications.objects.all()
    context = {        
        'licenses':lastmonthLicenses,
        'total_licenses':results1.count(),
        'total_blocked_licenses':results.count(),
    }
    return render(request,'core/reg-app.html',context)