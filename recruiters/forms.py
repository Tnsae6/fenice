from django import forms
from .models import Job, CompanyProfile


class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'job_type', 'link', 'dead_line']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }
        widgets = {
            'dead_line': forms.DateInput(attrs={'type': 'date'}),
        }


class CompanyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name', 'country', 'document']


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location',
                  'description', 'skills_req', 'job_type', 'link', 'dead_line']
        help_texts = {
            'skills_req': 'Enter all the skills required each separated by commas.',
            'link': 'If you want candidates to apply on your company website rather than on our website, please provide the link where candidates can apply. Otherwise, please leave it blank or candidates would not be able to apply directly!',
        }
        widgets = {
            'dead_line': forms.DateInput(attrs={'type': 'date'}),
        }