# Generated by Django 3.2 on 2021-04-26 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20210425_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloggers',
            options={},
        ),
        migrations.RemoveField(
            model_name='bloggers',
            name='user',
        ),
    ]
