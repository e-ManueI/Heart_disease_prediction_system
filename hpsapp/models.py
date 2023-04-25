from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_labtech = models.BooleanField(default=False)
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
