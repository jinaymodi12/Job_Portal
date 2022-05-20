# Generated by Django 4.0.4 on 2022-05-19 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_candidateprofile_user_jobpost_candidate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='candidate',
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.jobpost'),
        ),
    ]
