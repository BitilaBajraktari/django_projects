# Generated by Django 3.2 on 2021-04-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
    ]