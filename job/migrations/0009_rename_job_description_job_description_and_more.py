# Generated by Django 4.2.1 on 2023-05-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_time',
            new_name='type',
        ),
    ]
