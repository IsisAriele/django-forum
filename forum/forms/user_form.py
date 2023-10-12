from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=255)
    last_name = forms.CharField(label="Last name", max_length=255)
    username = forms.CharField(label="Username", max_length=255)
    email = forms.EmailField(label="E-mail", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=255)


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=255)
    