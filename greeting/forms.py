from django import forms
from .models import addshow,signup,login
class movieform(forms.ModelForm):
    class Meta:
        model=addshow
        fields='__all__'
class SignupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'
class LoginForm(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'
