# Generated by Django 3.2.16 on 2023-11-23 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20231123_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
    ]
