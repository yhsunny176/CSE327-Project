from django import forms
from .models import FreelancerProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = FreelancerProfile
        fields = ['age', 'address', 'skills', 'description', 'image']
