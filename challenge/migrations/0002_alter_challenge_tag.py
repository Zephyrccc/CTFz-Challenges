# Generated by Django 3.2.16 on 2022-11-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='tag',
            field=models.ManyToManyField(blank=True, to='challenge.Tag', verbose_name='标签'),
        ),
    ]