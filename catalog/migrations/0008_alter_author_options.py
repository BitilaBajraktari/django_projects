# Generated by Django 3.2 on 2021-04-21 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210421_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
    ]