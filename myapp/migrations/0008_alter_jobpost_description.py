# Generated by Django 4.0.4 on 2022-05-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_jobpost_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
