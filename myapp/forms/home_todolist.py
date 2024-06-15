# forms.py

from django import forms
from myapp.models import home_todolist_model

class home_todolistForm(forms.ModelForm):
    class Meta:
        model = home_todolist_model
        fields = ['status', 'task_name', 'due_date']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'task_name': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
