# Generated by Django 2.2.17 on 2021-01-17 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_closet_test_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='closet',
            name='test_image',
        ),
    ]
