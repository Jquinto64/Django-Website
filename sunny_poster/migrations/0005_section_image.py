# Generated by Django 2.2.5 on 2019-09-05 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunny_poster', '0004_remove_section_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image',
            field=models.ImageField(default='img/project1.png', upload_to='img/'),
            preserve_default=False,
        ),
    ]