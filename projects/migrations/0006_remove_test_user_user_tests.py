# Generated by Django 5.0.1 on 2024-01-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_test_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='tests',
            field=models.ManyToManyField(blank=True, to='projects.test'),
        ),
    ]
