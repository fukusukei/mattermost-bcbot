from django import forms
from .models import Register

class CreateRecord(forms.ModelForm):
    class Meta:
        model = Register
        widgets = {
            'Broadcast_messages': forms.Textarea(attrs={'rows':4, 'cols':60}),
            'Years': forms.Select,
            'Months': forms.Select,
            'Days': forms.Select,
            'Hours': forms.Select,
            'Minutes': forms.Select
        }
        labels = {
            'Broadcast_messages': 'Message'
        }

        fields = ['Broadcast_messages', 'Years', 'Months', 'Days', 'Hours', 'Minutes']
