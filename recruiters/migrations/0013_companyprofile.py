# Generated by Django 3.1.13 on 2023-06-16 06:14

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('recruiters', '0012_job_dead_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='companyprofile', serialize=False, to='auth.user')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, default='Ethiopia', max_length=2, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('document', models.FileField(blank=True, null=True, upload_to='documents')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='user', unique=True)),
            ],
        ),
    ]
