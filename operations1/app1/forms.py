from django import forms
class AdditionForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    place = forms.CharField(max_length=100, label="Place")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],label="Gender")
    role = forms.ChoiceField(choices=[('admin', 'Admin'), ('user', 'User')],label="Role")
    email = forms.EmailField(label="Email")

class CalorieForm(forms.Form):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)

    height = forms.IntegerField()
    weight = forms.IntegerField()
    age = forms.IntegerField()

    activity_choices = [
        ('1.2', 'sedentary'),
        ('1.375', 'lightly active'),
        ('1.55', 'moderately active'),
        ('1.725', 'very active'),
        ('1.9', 'extra active'),
    ]
    activity_levels = forms.ChoiceField(choices=activity_choices)

