# Generated by Django 3.0.6 on 2020-07-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20200709_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='designation',
            field=models.CharField(default=None, max_length=1500),
        ),
        migrations.AlterField(
            model_name='team',
            name='information',
            field=models.TextField(default=None, max_length=3000),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
