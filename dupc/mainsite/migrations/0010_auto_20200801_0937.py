# Generated by Django 2.2 on 2020-08-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_auto_20200709_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='department',
            field=models.CharField(default='HSS', max_length=1500),
        ),
        migrations.AddField(
            model_name='team',
            name='institute_name',
            field=models.CharField(default='IITG', max_length=1500),
        ),
    ]