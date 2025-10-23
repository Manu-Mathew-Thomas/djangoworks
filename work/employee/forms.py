from django import forms
from employee.models import Employeedetails

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employeedetails
        fields="__all__"