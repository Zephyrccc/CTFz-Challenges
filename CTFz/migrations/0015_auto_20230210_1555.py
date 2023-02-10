# Generated by Django 3.2.16 on 2023-02-10 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CTFz', '0014_challenge_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='captain',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamCaptain', to=settings.AUTH_USER_MODEL, verbose_name='队长'),
        ),
        migrations.CreateModel(
            name='SolveInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(choices=[(True, '成功'), (False, '失败')], default=False, verbose_name='解题状态')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='记录时间')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='题目')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CTFz.challenge', verbose_name='用户')),
            ],
            options={
                'verbose_name': '解题记录',
                'verbose_name_plural': '解题记录',
                'db_table': 'solve_info',
            },
        ),
        migrations.AddField(
            model_name='challenge',
            name='solve_user',
            field=models.ManyToManyField(through='CTFz.SolveInfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='solve_challenge',
            field=models.ManyToManyField(through='CTFz.SolveInfo', to='CTFz.Challenge'),
        ),
    ]
