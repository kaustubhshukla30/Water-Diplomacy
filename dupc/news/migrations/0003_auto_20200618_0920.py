# Generated by Django 3.0.6 on 2020-06-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200618_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
