from django.urls import path, reverse_lazy
from hpsapp.views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'hpsapp'

urlpatterns = [
    path('', LoginView.as_view(template_name='hpsapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/labtechnician/', LabTechnicianSignUpView.as_view(),
         name='labtechnician_signup'),
    path('signup/doctor/', DoctorSignUpView.as_view(), name='doctor_signup'),
    
    path('labtech/dashboard/', LabTechnicianDashboardView.as_view(), name='labtech_dashboard'),
    path('doctor/dashboard/', DoctorDashboardView.as_view(), name='doctor_dashboard'),
]
