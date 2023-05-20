from django.urls import path, reverse_lazy
from hpsapp.views import *
from django.contrib.auth.views import LogoutView

app_name = 'hpsapp'

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='hpsapp:login'), name='logout'),
    path('signup/labtechnician/', LabTechnicianSignUpView.as_view(),
         name='labtechnician_signup'),
    path('signup/doctor/', DoctorSignUpView.as_view(), name='doctor_signup'),
    
    path('labtech/dashboard/', LabTechnicianDashboardView.as_view(), name='labtech_dashboard'),
    path('doctor/dashboard/', DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('nurse/dashboard/', NurseDashboardView.as_view(), name='nurse_dashboard'),
    
    path('receptionist/dashboard/', ReceptionistDashboardView.as_view(), name='receptionist_dashboard'),
    
    # path('receptionist/patient/search/', SearchPatientView.as_view(), name='receptionist_search'),
    # path('receptionist/patient/<int:patient_id>/assign-doctor/', assign_doctor_to_patient, name='assign_doctor'),
    path('receptionist/patient/search/', SearchPatientView.as_view(), name='receptionist_search'),
    path('receptionist/patient/<int:patient_id/assign-doctor/', SearchPatientView.as_view(), name='assign_doctor'),
    
    path('patient/all/', PatientListView.as_view(), name='patient_list'),
    path('receptionist/patient/<int:patient_id>/assign-doctor/', assign_doctor_to_patient, name='assign_doctor_test'),
]
