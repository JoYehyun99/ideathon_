from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.forms.widgets import RadioSelect
from .models import UserInfo 

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserInfo
        fields = ['username','password1','password2','nickname','gender','age','school','major',
        'studentID','sleep_habit','sleep_time','cleanliness',
        'cook','smoke','budget','hope_area','introduction',
        'profile_active','profile_img',
        ]
        widgets = {
            'gender':forms.RadioSelect(),
            'sleep_habit':forms.RadioSelect(),
            'sleep_time': forms.RadioSelect(),
            'cleanliness':forms.RadioSelect(),
            'cook':forms.RadioSelect(),
            'budget':forms.RadioSelect()
        }