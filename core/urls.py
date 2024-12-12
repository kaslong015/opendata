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
    path('restricted-notblock-area/', RestrictedNotblocksLicensingAreaListView.as_view(), name='restricted-area-notblock'),
    path('register/', RegisterPage.as_view(), name="register"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('valid-license/<slug:pk>/', ValidDetailView.as_view(), name='valid-detail'),
    path('block-license/<str:pk>/', BlockDetailView.as_view(), name='block-detail'),
    path('last-license/<str:pk>/',  LastMonthDetailView.as_view(), name='last-detail'),
    path('restricted/all/',RestrictedAreaListView.as_view(), name='restricted-all'),
    path('load-coordinates/<str:record_id>/', LoadCoordinatesView.as_view(), name='load_coordinates'),
    path('restricted-area/<str:pk>/', RestrictedAreaDetailView.as_view(), name='restricted-area'),
    path('restricted-block-area/', RestrictedblocksLicensingAreaListView.as_view(), name='restricted-area-block'),
    path('other-restricted-area/', OtherRestrictedblockedLicensingAreaListView.as_view(), name='other-restricted-area'),
    path('load-coordinates/', load_coordinates, name='load_coordinates'),    
    path('map/', maps, name='map'),
    path('geojsonmap/',geological_map, name='geological_map'),
]

