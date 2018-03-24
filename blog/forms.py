from django import forms
from .models import Post

# PostForm, as you probably suspect, is the name of our form. We need to tell Django that 
# this form is a ModelForm (so Django will do some magic for us) forms.ModelForm is responsible for that

class PostForm(forms.ModelForm):
  # tell Django which model should be used to create this form (model = Post).
  class Meta:
    model = Post
    fields = ('title', 'text')