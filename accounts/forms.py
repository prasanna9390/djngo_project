from django import forms
from accounts.models import User,UserProfile

class userform(forms.ModelForm):
    class Meta:
        model= User
        fields=['first_name','last_name','username','email','phone_number','password']