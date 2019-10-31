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
        exclude = ['profile','comments','name','user','likes','design','usability','content']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }       
class newReviewForm(forms.ModelForm):
   class Meta:
        model = Project
        exclude = ['image','title','description','post','profile','user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }       
