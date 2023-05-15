# Generated by Django 4.2 on 2023-05-15 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hpsapp', '0007_patient_user_is_patient_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receptionist',
                'verbose_name_plural': 'Receptionists',
            },
        ),
        migrations.AddField(
            model_name='result',
            name='blood_pressure',
            field=models.FloatField(help_text='(mmHg)', null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='height',
            field=models.FloatField(help_text='(cm)', null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='weight',
            field=models.FloatField(help_text='(kg)', null=True),
        ),
    ]