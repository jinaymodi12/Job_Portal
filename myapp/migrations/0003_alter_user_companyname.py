# Generated by Django 4.0.4 on 2022-05-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='companyname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
