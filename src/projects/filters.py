import django_filters
from django.forms import TextInput, Select, DateInput
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='عنوان المشروع',
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ابحث عن عنوان المشروع...'
        })
    )
    state = django_filters.ChoiceFilter(
        field_name='state',
        choices=[
            ('inprogress', 'قيد التنفيذ'),
            ('completed', 'مكتمل'),
            ('pending', 'معلق')
        ],
        label='حالة المشروع',
        widget=Select(attrs={
            'class': 'form-select'
        })
    )
    created_at = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='exact',
        label='تاريخ الإنشاء',
        widget=DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    class Meta:
        model = Project
        fields = ['title', 'state', 'created_at']
