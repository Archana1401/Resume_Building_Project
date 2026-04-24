from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

        widgets = {
            'career_objective': forms.Textarea(attrs={'rows':3}),
            'education': forms.Textarea(attrs={'rows':3}),
            'technical_skills': forms.Textarea(attrs={'rows':3}),
            'projects': forms.Textarea(attrs={'rows':5}),
            'certifications': forms.Textarea(attrs={'rows':3}),
            'soft_skills': forms.Textarea(attrs={'rows':3}),
        }