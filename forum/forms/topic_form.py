from django import forms

class TopicRegistrationForm(forms.Form):
    title = forms.CharField(label="Title", max_length=500)
    text = forms.CharField(label="Description", widget=forms.Textarea(attrs={"rows":"10"}))
