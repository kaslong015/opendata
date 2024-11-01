from .models import *

def blocked_context(request):
    block = blockedLicenses.objects.all().count
    registed = registeredApplications.objects.all().count()
    pending = pendingApplications.objects.all().count()
    total_licenses = Licenses.objects.all().count

    return {

        'blocked': block,
        'total_licenses':total_licenses,                       
        'registed':registed,
        'pending':pending        
    }

