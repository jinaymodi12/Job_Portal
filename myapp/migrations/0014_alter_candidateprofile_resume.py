# Generated by Django 4.0.4 on 2022-05-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_candidateprofile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='resume',
            field=models.FileField(default=1, upload_to='profile'),
            preserve_default=False,
        ),
    ]
