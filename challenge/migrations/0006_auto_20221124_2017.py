# Generated by Django 3.2.16 on 2022-11-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_auto_20221124_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challengeattachment',
            old_name='challenge',
            new_name='challenge_one',
        ),
        migrations.RenameField(
            model_name='challengedockerconfig',
            old_name='challenge',
            new_name='challenge_two',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='describe',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='have_attachment',
            field=models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='是否有附件'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='is_fixed_flag',
            field=models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='flag是否固定'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='state',
            field=models.BooleanField(choices=[(True, '开放'), (False, '隐藏')], verbose_name='状态'),
        ),
    ]
