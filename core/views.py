from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def dashboard(request):
    results = Licenses.objects.all().order_by('id')
    

    context = {        
        'licenses':results,
        'total_licenses':results.count(),
    }
    return render(request,'core/dashboard.html',context)