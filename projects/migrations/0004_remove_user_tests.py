# Generated by Django 5.0.1 on 2024-01-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_test_user_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tests',
        ),
    ]