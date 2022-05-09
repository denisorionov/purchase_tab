from django.forms import forms

"""
class RequestForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio',
                  'owner']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'custom-select mr-sm-2'}, choices=STATUS_CHOICES),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.Select(attrs={'class': 'custom-select mr-sm-2'}, choices=SPECIALTY_CHOICES),
            'grade': forms.Select(attrs={'class': 'custom-select mr-sm-2'}, choices=GRADE_CHOICES),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'portfolio': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.HiddenInput()

        }

"""