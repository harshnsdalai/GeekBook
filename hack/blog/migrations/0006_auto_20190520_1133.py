# Generated by Django 2.1.2 on 2019-05-20 06:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190520_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 6, 3, 38, 676123, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 6, 3, 38, 676123, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
