# Generated by Django 4.2 on 2023-05-16 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpsapp', '0010_patientappointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='department',
            new_name='specialization',
        ),
    ]