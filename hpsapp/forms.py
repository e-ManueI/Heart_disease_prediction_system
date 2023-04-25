from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


# Sign Up form for Labtech
class LabtechSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

# Sign Up form for Doctor
class DoctorSignUpForm(UserCreationForm):
    department = forms.CharField(max_length=25)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('department',)