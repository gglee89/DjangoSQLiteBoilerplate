from django import forms

class InstaloaderForm(forms.Form):
    user = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
    shortCode = forms.CharField(label='Shortcode')