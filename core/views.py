from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import RedirectView, ListView, UpdateView, DeleteView, FormView, DetailView,View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from collections import defaultdict
from django.views.decorators.cache import cache_page
from pathlib import Path
import csv
import json
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent


def geological_map(request):
    return render(request, 'geojsonmap.html')

def load_coordinates(request):
    # Update this path to your CSV file location
    file_path = BASE_DIR /'converted_coordinates1_output.csv'  
    data_dict = defaultdict(list)

    # Read the CSV file and populate the dictionary
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if exists

        for row in reader:
            # print(row)
            id_, lat, lng = row[0], float(row[1]), float(row[2])
            data_dict[id_].append({"lat": lat, "lng": lng})

    return JsonResponse(data_dict)

# Create your views here.
@login_required(login_url='login')
@cache_page(60 * 30)
def dashboard(request):
    results = Licenses.objects.all().order_by('id')   
    yearly = [int(x.year) for x in YearlyCount.objects.all()]
    total_yearly_count = [int(x.total) for x in YearlyCount.objects.all()]
    # print(total_yearly_count)
    context = {        
        'licenses':results,        
        'years':yearly,
        'total_count':total_yearly_count
    }
    return render(request,'core/dashboard.html',context)

def maps(request):    
    return render(request,'maps.html')

@login_required(login_url='login')
def blocked_licenses_view(request):
    results = blockedLicenses.objects.all()   
    context = {        
        'licenses':results,        
    }
    return render(request,'core/block.html',context)

@login_required(login_url='login')
def registed_measures_view(request):    
   
    measures = registered_measures.objects.all()     
    context = {        
        'measures':measures,
        
    }
    return render(request,'core/registed_measure.html',context)

@login_required(login_url='login')
def last_month_view(request):
    
    lastmonthLicenses = lastMonthLicenses.objects.all()   
    context = {        
        'licenses':lastmonthLicenses,
        
    }
    return render(request,'core/lastmonth.html',context)


@login_required(login_url='login')
def pending_measures_view(request):
    
    lastmonthLicenses = pendingMeasures.objects.all()
    
    context = {        
        'licenses':lastmonthLicenses,
        
    }
    return render(request,'core/pending_measure.html',context)


@login_required(login_url='login')
def pending_application_view(request):
   
    lastmonthLicenses = pendingApplications.objects.all()   
    context = {        
        'licenses':lastmonthLicenses,       
        
    }
    return render(request,'core/pen-app.html',context)


@login_required(login_url='login')
def register_application_view(request):  

    Licenses = registeredApplications.objects.all()   
    context = {        
        'licenses':Licenses,        
        
    }
    return render(request,'core/reg-app.html',context)



class RegisterPage(FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    # redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class Login(LoginView):
    template_name = 'core/login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')
    

class LogoutView(RedirectView):
    
    """
    Provides users the ability to logout
    """

    url = '/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ValidDetailView(DetailView,LoginRequiredMixin):
    model = Licenses
    template_name = 'core/details/detail.html'
    context_object_name = 'license'

    def get_context_data(self, **kwargs):
        # Get the default context data from the parent class
        context = super().get_context_data(**kwargs)
        
        # Get all coordinates with code and return them as context in the view
        latLog = Coordinates.objects.filter(code=context['license'])
        
        #adding contetx name to the context object  
        context['cords'] = latLog  
        
        # You can add more context as needed
        return context


class BlockDetailView(DetailView,LoginRequiredMixin):
    model = blockedLicenses
    template_name = 'core/details/block.html'
    context_object_name = 'license'


class LastMonthDetailView(DetailView,LoginRequiredMixin):
    model = lastMonthLicenses
    template_name = 'core/details/lastmonth.html'
    context_object_name = 'license'
    

class RestrictedAreaDetailView(DetailView,LoginRequiredMixin):
    model = RestrictedAreas
    template_name = 'core/restricted/restricted-deatil.html'
    context_object_name = 'license'

class RestrictedAreaListView(ListView,LoginRequiredMixin):
    model = RestrictedAreas
    context_object_name = 'restrictedareas'   # your own name for the list as a template variable
    queryset = RestrictedAreas.objects.all() 
    template_name = 'core/restricted/allareas.html'  


class RestrictedblocksLicensingAreaListView(ListView,LoginRequiredMixin):
    model = RestrictedAreas
    context_object_name = 'blockingrestricedareas'   # your own name for the list as a template variable
    queryset = RestrictedAreas.objects.all().filter(type='Restricted area (blocks licensing)')    
    template_name = 'core/restricted/restricted-block.html' 


class RestrictedNotblocksLicensingAreaListView(ListView,LoginRequiredMixin):
    model = RestrictedAreas
    context_object_name = 'notblockingrestricedareas'   # your own name for the list as a template variable
    queryset = RestrictedAreas.objects.all().filter(type='Restricted area (does not block licensing)')    
    template_name = 'core/restricted/notrestricted-blocked.html' 


class OtherRestrictedblockedLicensingAreaListView(ListView,LoginRequiredMixin):
    model = RestrictedAreas
    context_object_name = 'otherrestricedareas'   # your own name for the list as a template variable
    queryset = RestrictedAreas.objects.all().filter(type='Other restricted area (does not block licensing)')
    template_name = 'core/restricted/other-restricted.html'



class LoadCoordinatesView(View):
    def get(self, request, record_id):
        # Load data from the CSV file
        path_to_file =  BASE_DIR /'converted_coordinates1_output.csv'  
        df = pd.read_csv(path_to_file, header=None, names=["ID","Latitude_Decimal","Longitude_Decimal"])
        
        # Filter data by record_id
        filtered_data = df[df['ID'] == record_id]

        # Convert to JSON format expected by Leaflet
        coordinates = [{"lat": row.Latitude_Decimal, "lng": row.Longitude_Decimal} for _, row in filtered_data.iterrows()]
        response_data = {record_id: coordinates}
        
        return JsonResponse(response_data)


