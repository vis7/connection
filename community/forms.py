from django import forms
from .models import Community

class CommunityForm(forms.ModelForm):
    
    class Meta:
        model = Community
        fields = [
            'name',
            'admin_id',
            'rules',
            'description',
        ]

