# Generated by Django 3.2.16 on 2023-11-23 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_comments_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comments_count',
        ),
    ]