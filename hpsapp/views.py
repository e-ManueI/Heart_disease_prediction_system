from .forms import DoctorSignUpForm, LabtechSignUpForm
from .models import LabTechnician, Doctor, User, Patient
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Q
from functools import reduce
from django.core.paginator import Paginator


############################################################################################
#                                   GENERAL VIEWS
############################################################################################
class CustomLoginView(LoginView):
    template_name = 'hpsapp/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.is_labtech:
            self.next_page = 'hpsapp:labtech_dashboard'
        elif user.is_doctor:
            self.next_page = 'hpsapp:doctor_dashboard'
        elif user.is_nurse:
            self.next_page = 'hpsapp:nurse_dashboard'
        elif user.is_receptionist:
            self.next_page = 'hpsapp:receptionist_dashboard'
        else:
            self.next_page = 'hpsapp:login'
            
        return super().form_valid(form)

############################################################################################
#                                   MIXINS
############################################################################################
class DoctorRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "Doctor access only"

    def test_func(self):
        return self.request.user.is_doctor
    
class LabtechRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "LabTech access only"

    def test_func(self):
        return self.request.user.is_labtech
    
class NurseRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "Nurse access only"

    def test_func(self):
        return self.request.user.is_nurse

class ReceptionistRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "Receptionist access only"

    def test_func(self):
        return self.request.user.is_receptionist
    
############################################################################################
#                                   LABTECH'S VIEWS
############################################################################################
class LabTechnicianSignUpView(CreateView):
    form_class = LabtechSignUpForm
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

        return redirect('hpsapp:login')
    
    def form_invalid(self, form):
        # Print the form errors to the console
        print(form.errors)

        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lab Technician Signup'
        return context
    
class LabTechnicianDashboardView(LoginRequiredMixin, LabtechRequiredMixin, TemplateView):
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
    form_class = DoctorSignUpForm
    template_name = 'hpsapp/signup.html'
    success_url = reverse_lazy('hpsapp:login')

    def form_valid(self, form):
        # Save the user object
        user = form.save(commit=False)
        user.is_doctor = True
        user = form.save()

        # Create a new Doctor object for the user
        doctor = Doctor.objects.create(user=user, department=form.cleaned_data.get('department'))
        return redirect('hpsapp:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Doctors Signup'
        return context
    

class DoctorDashboardView(LoginRequiredMixin, DoctorRequiredMixin, TemplateView):
    template_name = 'hpsapp/doctor_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Doctor Dashboard'
        return context
    

############################################################################################
#                                   RECEPTIONIST'S VIEWS
############################################################################################
class ReceptionistDashboardView(LoginRequiredMixin, ReceptionistRequiredMixin, TemplateView):
    template_name = 'hpsapp/receptionist_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Receptionist Dashboard'
        return context
    
# correct search view
class SearchPatientView(View):
    def get(self, request):
        query = request.GET.get('q')
        if not query:
            messages.warning(request, 'Please enter a search query')
            return redirect('hpsapp:receptionist_dashboard')
        words = query.split()
        results = Patient.objects.filter(
            reduce(lambda x, y: x | y, [
                Q(user__username__icontains=word) |
                Q(user__first_name__icontains=word) |
                Q(user__last_name__icontains=word)
                for word in words])
            ).distinct()
        if not results:
            messages.warning(request, 'No results found for query: {}'.format(query))
            return redirect('hpsapp:receptionist_dashboard')
        paginator = Paginator(results, 3)  # Show 3 results per page
        page = request.GET.get('page')
        results = paginator.get_page(page)
        context = {
            'results': results,
            'title': 'Receptionist Dashboard',
        }
        return render(request, 'hpsapp/receptionist_patient_list.html', context=context)
    
############################################################################################
#                                   NURSES'S VIEWS
############################################################################################
class NurseDashboardView(LoginRequiredMixin, NurseRequiredMixin, TemplateView):
    template_name = 'hpsapp/nurse_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nurse Dashboard'
        return context