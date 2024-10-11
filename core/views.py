from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import RedirectView, ListView, UpdateView, DeleteView, FormView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    results = Licenses.objects.all().order_by('id')
    blocked = blockedLicenses.objects.all().count()
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    yearly = [int(x.year) for x in YearlyCount.objects.all()]
    total_yearly_count = [int(x.total) for x in YearlyCount.objects.all()]
    print(total_yearly_count)
    context = {        
        'licenses':results,
        'total_licenses':results.count(),
        'blocked':blocked,
        'registed':registed,
        'pending':pending,
        'years':yearly,
        'total_count':total_yearly_count
    }
    return render(request,'core/dashboard.html',context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
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


class ValidDetailView(DetailView):
    model = Licenses
    template_name = 'core/details/detail.html'
    context_object_name = 'license'


class BlockDetailView(DetailView):
    model = blockedLicenses
    template_name = 'core/details/block.html'
    context_object_name = 'license'


class LastMonthDetailView(DetailView):
    model = lastMonthLicenses
    template_name = 'core/details/lastmonth.html'
    context_object_name = 'license'
    