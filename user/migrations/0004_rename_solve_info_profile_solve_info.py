# Generated by Django 3.2.16 on 2022-11-25 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20221125_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Solve_Info',
            new_name='solve_info',
        ),
    ]
