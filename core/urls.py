from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name="dashboard" ),
    path('blocked/',blocked_licenses_view,name="blocked" ),
    path('last_month/',last_month_view,name="last" ),
    path('reg_measure/',registed_measures_view,name='reg_mes'),
    path('pen_measure/',pending_measures_view,name='pen_mes'),
    path('reg_application/',register_application_view,name='reg_app'),
    path('pen_application/',pending_application_view,name='pen_app'),
    path('register/', RegisterPage.as_view(), name="register"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

