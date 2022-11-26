from django import forms
from .models import DjangoHub

class ResourcesForm(forms.ModelForm):
    class Meta:
        model = DjangoHub
        fields = ('name', 'link', 'tags', 'format', 'difficulty', 'time')
        labels = {
            'name' : 'Name',
            'link' : 'Link',
            'tags' : 'Tags',
        }

        widget = {
            'name': forms.TimeInput(attrs={'placeholder': 'Name'}),
            'link': forms.TimeInput(attrs={'placeholder': 'Link'}),
            'tags': forms.TimeInput(attrs={'placeholder': 'Tags'}),
        }

    def __init__(self, args, **kwargs):
        super(ResourcesForm, self) .__init__(*args, **kwargs)
        self.field['format'].choices = "Select format"
        self.field['difficulty'].choices = "Select difficulty"
        self.field['time'].choices = "Select time"