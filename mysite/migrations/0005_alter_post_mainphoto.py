# Generated by Django 4.1.2 on 2022-11-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_post_mainphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
