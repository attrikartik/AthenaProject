from django import forms
from .models import *


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
