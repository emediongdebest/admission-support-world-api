# Generated by Django 4.0.6 on 2022-07-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '3. Courses'},
        ),
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name_plural': '2. Course Categories'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '4. Students'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': '1. Teachers'},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='address',
            new_name='skills',
        ),
        migrations.AddField(
            model_name='student',
            name='interested_category',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
