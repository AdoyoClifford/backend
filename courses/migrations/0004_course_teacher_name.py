# Generated by Django 5.0 on 2024-06-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]