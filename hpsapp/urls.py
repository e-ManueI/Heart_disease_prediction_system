from django.urls import path, reverse_lazy
from hpsapp.views import *
from django.contrib.auth.views import LogoutView

app_name = 'hpsapp'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/labtechnician/', LabTechnicianSignUpView.as_view(),
         name='labtechnician_signup'),
    path('signup/doctor/', DoctorSignUpView.as_view(), name='doctor_signup'),
    
    path('labtech/dashboard/', LabTechnicianDashboardView.as_view(), name='labtech_dashboard'),
    path('doctor/dashboard/', DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('nurse/dashboard/', NurseDashboardView.as_view(), name='nurse_dashboard'),
    
    path('receptionist/dashboard/', ReceptionistDashboardView.as_view(), name='receptionist_dashboard'),
    path('receptionist/search_patient/', SearchPatientView.as_view(), name='receptionist_search'),
]
