from django.contrib import admin
from .models import Job, Applicants, Selected, CompanyProfile

admin.site.register(Job)
admin.site.register(Selected)
admin.site.register(Applicants)
admin.site.register(CompanyProfile)
