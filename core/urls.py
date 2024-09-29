from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name="dashboard" ),
    path('blocked/',blocked_licenses_view,name="blocked" ),
     path('last_month/',last_month_view,name="last" ),
]

