# Generated by Django 3.2.16 on 2023-02-09 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CTFz', '0003_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
    ]
