# Generated by Django 3.2.16 on 2023-08-09 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20230809_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='future_date',
        ),
    ]
