from django import forms
from .models import GymMember

class MembershipForm(forms.ModelForm):
    class Meta:
        model = GymMember
        fields = ['full_name', 'email', 'phone', 'age', 'gender', 'membership_type']
        widgets = {
            'membership_type': forms.Select(attrs={'class': 'form-control'}),
        }
