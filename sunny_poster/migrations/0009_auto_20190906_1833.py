# Generated by Django 2.2.5 on 2019-09-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunny_poster', '0008_auto_20190906_1807'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acknowledgements',
        ),
        migrations.DeleteModel(
            name='Clinical_Motivation',
        ),
        migrations.AddField(
            model_name='section',
            name='image',
            field=models.FilePathField(default='', path='/img'),
            preserve_default=False,
        ),
    ]
