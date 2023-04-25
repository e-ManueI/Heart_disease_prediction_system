from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import LabTechnician, Doctor, User
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

############################################################################################
#                                   GENERAL VIEWS
############################################################################################
class CustomLoginView(LoginView):
    template_name = 'hpsapp/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated and user.is_doctor:
            return reverse_lazy('doctor_dashboard')
        elif user.is_authenticated and user.is_labtech:
            return reverse_lazy('labtech_dashboard')
        else:
            return super().get_success_url()


############################################################################################
#                                   LABTECH'S VIEWS
############################################################################################
class LabTechnicianSignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'hpsapp/signup.html'
    success_url = reverse_lazy('hpsapp:login')

    def form_valid(self, form):
        # Save the user object
        user = form.save(commit=False)
        user.is_labtech = True
        print(user)
        user.save()

        # Create a new LabTechnician object for the user
        labtech = LabTechnician.objects.create(user=user)
        labtech.save()

        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Print the form errors to the console
        print(form.errors)

        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lab Technician Signup'
        return context
    
class LabTechnicianDashboardView(TemplateView):
    template_name = 'hpsapp/labtech_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lab Technician Dashboard'
        return context
    

############################################################################################
#                                   DOCTOR'S VIEWS
############################################################################################
class DoctorSignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'hpsapp/signup.html'
    success_url = reverse_lazy('hpsapp:login')

    def form_valid(self, form):
        # Save the user object
        user = form.save(commit=False)
        user.is_doctor = True
        user.save()

        # Create a new Doctor object for the user
        doctor = Doctor.objects.create(user=user)
        doctor.save()

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Doctors Signup'
        return context
    
    
class DoctorDashboardView(TemplateView):
    template_name = 'hpsapp/doctor_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Doctor Dashboard'
        return context
    
