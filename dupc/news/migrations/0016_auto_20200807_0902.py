# Generated by Django 2.2 on 2020-08-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]