# Generated by Django 4.0.4 on 2022-05-20 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_candidateprofile_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateprofile',
            name='resume',
        ),
    ]
