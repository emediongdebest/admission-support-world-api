# Generated by Django 4.0.6 on 2022-08-08 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_teacher_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='otp_digit',
        ),
        migrations.RemoveField(
            model_name='student',
            name='verify_status',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='otp_digit',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='verify_status',
        ),
    ]
