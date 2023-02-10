# Generated by Django 3.2.16 on 2023-02-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTFz', '0008_remove_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/defaultAvatar.png', upload_to='avatar', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(default='这家伙很懒什么也没留下...', max_length=254, verbose_name='个人介绍'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女'), ('保密', '保密')], default='保密', max_length=2, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='total_score',
            field=models.PositiveIntegerField(default=0, verbose_name='总分'),
        ),
    ]
