from django import forms
from .models import Profile,Project

class ProfileForm(forms.ModelForm):
   class Meta:
        model = Profile
        exclude = ['']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class newPostForm(forms.ModelForm):
   class Meta:
        model = Project
        exclude = ['profile','comments','name','user','likes']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }       
