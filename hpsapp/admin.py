from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

# TODO: Add admin views for all models to add users
# Register your models here.
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = '__all__'
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'is_doctor', 'is_nurse', 'is_receptionist', 'is_labtech')

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = ('username', 'is_patient', 'is_doctor', 'is_nurse', 'is_receptionist', 'is_labtech')

#     def save_model(self, request, obj, form, change):
#         if 'is_nurse' in form.changed_data and obj.is_nurse:
#             nurse = Nurse.objects.create(user=obj)
#         elif 'is_receptionist' in form.changed_data and obj.is_receptionist:
#             receptionist = Receptionist.objects.create(user=obj)
#         elif 'is_doctor' in form.changed_data and obj.is_doctor:
#             doctor = Doctor.objects.create(user=obj)
#         elif 'is_patient' in form.changed_data and obj.is_patient:
#             patient = Patient.objects.create(user=obj)
#         elif 'is_labtech' in form.changed_data and obj.is_labtech:
#             labtech = LabTechnician.objects.create(user=obj)
#         obj.save()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    SEX_CHOICES = (
        (True, 'Male'),
        (False, 'Female'),
    )
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    
class PatientAdmin(admin.ModelAdmin):
    form = PatientForm


admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(LabTechnician)
admin.site.register(Receptionist)
admin.site.register(Nurse)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PreConsultationTest)
admin.site.register(DiagnosticTest)
admin.site.register(PatientAppointment)
