# Generated by Django 2.2.5 on 2019-09-07 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunny_poster', '0009_auto_20190906_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='image',
        ),
    ]
