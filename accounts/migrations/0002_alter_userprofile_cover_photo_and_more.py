# Generated by Django 5.0.2 on 2024-02-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/cover_photos'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_pictures'),
        ),
    ]
