# Generated by Django 3.2.16 on 2023-02-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTFz', '0010_auto_20230210_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='是否是管理员'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='账号状态'),
        ),
    ]