# Generated by Django 5.1.5 on 2025-01-30 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
