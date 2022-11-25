# Generated by Django 3.2.16 on 2022-11-25 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女'), ('保密', '保密')], default='保密', max_length=2, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='solve_info',
            field=models.ManyToManyField(through='user.SolveInfo', to='challenge.Challenge', verbose_name='解题记录'),
        ),
        migrations.AlterField(
            model_name='solveinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]