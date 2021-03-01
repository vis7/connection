from django import forms

from .models import Advertisement

class AdvertiserForm(forms.ModelForm):
    
    class Meta:
        model = Advertisement
        fields = [
            'content',
            'text_description',
            'audience_details',
            'advertise_id',
            'advertisement_link',
            'user_preference',
            'money_credit',
            'view_need_to_shown',
            'user_who_watched',
        ]

