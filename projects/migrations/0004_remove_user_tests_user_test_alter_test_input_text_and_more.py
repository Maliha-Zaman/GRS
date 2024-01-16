# Generated by Django 4.2.6 on 2024-01-15 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_test_user_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tests',
        ),
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='input_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='output_text',
            field=models.TextField(),
        ),
    ]
