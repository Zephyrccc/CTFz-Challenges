# Generated by Django 3.2.16 on 2023-02-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTFz', '0017_auto_20230210_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(choices=[(True, '正常'), (False, '封禁')], default=True, verbose_name='账号状态'),
        ),
    ]
