# Generated by Django 5.0.3 on 2024-03-31 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_post_header_image_profile_facebook_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='header_image',
            new_name='profile_pic',
        ),
    ]
