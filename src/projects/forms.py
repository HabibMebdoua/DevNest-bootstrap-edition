from django.forms import ModelForm
from django import forms
from projects.models import Project


class OrderProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'ppt_presentation', 'tech_card']
        labels = {
            'title': 'عنوان المشروع',
            'description': 'وصف المشروع',
            'type': 'نوع المشروع',
            'ppt_presentation': 'هل تريد عرض تقديمي خاصة بالمشروع؟',
            'tech_card': 'هل تريد بطاقة تقنية خاصة بالمشروع؟',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان المشروع'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'وصف المشروع',
                'rows': 4,
            }),
            'type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'ppt_presentation': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'tech_card': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
