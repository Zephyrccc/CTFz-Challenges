# Generated by Django 3.2.16 on 2023-02-10 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CTFz', '0007_auto_20230210_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
    ]
