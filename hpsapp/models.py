from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_labtech = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    phone_number = models.CharField(
        max_length=15, verbose_name="Phone Number", null=True)
    
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set', verbose_name=('groups'), help_text=(
        'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),)
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set', verbose_name=(
        'user permissions'), help_text=('Specific permissions for this user.'),)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

class LabTechnician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Lab Technician'
        verbose_name_plural = 'Lab Technicians'
        
class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Receptionist'
        verbose_name_plural = 'Receptionists'
        
class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Nurse'
        verbose_name_plural = 'Nurses'
        
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.BooleanField(null=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

class PreConsultationTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    height = models.FloatField(null=True, help_text="(cm)")
    weight = models.FloatField(null=True, help_text="(kg)")
    systolic_pressure = models.FloatField(null=True, blank=True, help_text="Systolic blood pressure in mmHg")
    diastolic_pressure = models.FloatField(null=True, blank=True, help_text="Diastolic blood pressure in mmHg")
    recorded_by = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    recorded_at = models.DateTimeField(auto_now_add=True)
    
class DiagnosticTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    labtech = models.ForeignKey(LabTechnician, on_delete=models.CASCADE)
    anaemia = models.BooleanField(null=True)
    high_blood_pressure = models.BooleanField(null=True)
    diabetes = models.BooleanField(null=True)
    smoking = models.BooleanField(null=True)
    creatine_phosphokinase = models.FloatField(null=True, help_text="CPK enzyme level (mcg/L)")
    ejection_fraction = models.FloatField(null=True, help_text="Percentage of blood leaving the heart at each contraction (percentage)")
    platelets = models.FloatField(null=True, help_text="(kiloplatelets/mL)")
    serum_creatinine = models.FloatField(null=True, help_text="(mg/dL)")
    serum_sodium = models.FloatField(null=True, help_text="(mEq/L)")
    death_event = models.BooleanField(null=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    
class PatientAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField(auto_now_add=True)
    status_choices = (
        ('R', 'Registred - In pre-consultation'),
        ('P', 'Pre-consultated - In consultation'),
        ('C', 'Consulted - Awaiting Diagnostic test'),
        ('D', 'Diagnostic tested - Awaiting Feedback'),
        ('F', 'Feedback'),
    )
    status = models.CharField(max_length=1, choices=status_choices, default='R')
    preconsultation_test = models.OneToOneField(PreConsultationTest, on_delete=models.SET_NULL, null=True, blank=True)
    diagnostic_test = models.OneToOneField(DiagnosticTest, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient.user.username} - {self.doctor.user.username}"
