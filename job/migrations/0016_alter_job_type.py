# Generated by Django 4.2.1 on 2023-05-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_job_owner_alter_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=15),
        ),
    ]