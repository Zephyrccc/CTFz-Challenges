# Generated by Django 3.2.16 on 2022-11-25 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='tag',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
    ]
