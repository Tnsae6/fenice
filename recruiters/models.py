from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils import timezone

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)


class CompanyProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name='companyprofile')
    name = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField(null=True, blank=True, default='Ethiopia')
    verified = models.BooleanField(default = False)
    document = models.FileField(upload_to='resumes', null=True, blank=True)

    slug = AutoSlugField(populate_from='user', unique=True)

    def get_absolute_url(self):
        return "/company_profile/{}".format(self.slug)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    recruiter = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField()
    skills_req = models.CharField(max_length=200)
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    dead_line = models.DateTimeField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(
        Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant
