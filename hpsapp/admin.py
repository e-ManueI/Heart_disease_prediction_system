from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(LabTechnician)
admin.site.register(Receptionist)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(PreConsultationTest)
admin.site.register(DiagnosticTest)
admin.site.register(PatientAppointment)
