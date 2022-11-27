from django import forms 
from .models import Resources


class ResourcesForm(forms.ModelForm):
  class Meta:
    model = Resources
    fields = ['name', 'link', 'tags', 'format', 'difficulty', 'time']
    labels = {
      'name': 'Name', 
      'link': 'Link', 
      'tags': 'Tags', 
      'format': 'Format', 
      'difficulty': 'Difficulty', 
      'time': 'Estimated Time of Completion'
    }
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'link': forms.TextInput(attrs={'class': 'form-control'}),
      'tags': forms.TextInput(attrs={'class': 'form-control'}),
      'format': forms.TextInput(attrs={'class': 'form-control'}),
      'difficulty': forms.TextInput(attrs={'class': 'form-control'}),
      'time': forms.TextInput(attrs={'class': 'form-control'}),
    }