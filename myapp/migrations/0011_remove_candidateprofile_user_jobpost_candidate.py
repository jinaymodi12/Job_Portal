# Generated by Django 4.0.4 on 2022-05-19 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_candidateprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='candidate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.candidateprofile'),
        ),
    ]