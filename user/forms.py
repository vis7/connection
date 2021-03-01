from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Advertiser

# defineing custom widget for rendering html form with that widget
class DateInput(forms.DateInput):
    input_type = 'date'

class UserModelForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = "__all__" #[
            
            # 'username',
            # 'dob',
            # 'location',
            # 'country',
            # 'mobile',
            # 'email',
            # 'gender',
            # 'password',
        # ]
        widgets = {
            'dob': DateInput()
        }

class UserProfileModelForm(UserChangeForm):
# class UserProfileModelForm(forms.Form):
    class Meta:
        model = User
        fields = [
            # 'username',
            # 'dob',
            # 'location',
            # 'country',
            # 'mobile',
            # 'email',
            # 'gender',
            'language',
            'relationship_status',
            'hobbies',
            'movies',
            'tv_shows',
            'books',
            'profile_pic',
            'cover_pic',
            'friends',
            'user_community',
        ]
        widgets = {
            'dob': DateInput()
        }

class AdvertiserModelForm(forms.ModelForm):
    
    class Meta:
        model = Advertiser
        fields = [
            # 'username',
            # 'dob',
            # 'location',
            # 'country',
            # 'mobile',
            # 'email',
            # 'gender',
            # 'password',
            'balance',
        ]
        widgets = {
            'dob': DateInput()
        }