# Generated by Django 4.0.4 on 2022-05-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_jobpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='position',
            field=models.CharField(max_length=200),
        ),
    ]
