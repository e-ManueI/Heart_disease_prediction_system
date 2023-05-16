# Generated by Django 4.2 on 2023-05-16 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hpsapp', '0011_rename_department_doctor_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hpsapp.doctor'),
        ),
    ]