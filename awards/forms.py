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
class newReviewForm(forms.ModelForm):
   class Meta:
      #   model = Review
        fields = ['usability_rating','content_rating','design_rating','comment']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }       
