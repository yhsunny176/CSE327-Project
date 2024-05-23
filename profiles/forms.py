from django import forms
<<<<<<< Updated upstream
from .models import UserProfile

# Define form for updating UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Use UserProfile model
        fields = ['age', 'address', 'skills', 'description', 'image']  # Fields to include in the form

        # Custom widget for description field
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
=======
from .models import FreelancerProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = FreelancerProfile
        fields = ['age', 'address', 'skills', 'description', 'image']
>>>>>>> Stashed changes
