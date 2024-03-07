# from django import forms 
# from .models import Employee
# class form1(forms.Form):
#     class Meta:
#         model=Employee 
#         fields='__all__'
#     # email=forms.CharField(min_length=10,max_length=100)
#     # password=forms.CharField(min_length=10,max_length=100) 


from django import forms
from .models import Customer 
class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'password']