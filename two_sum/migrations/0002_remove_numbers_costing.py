# Generated by Django 4.0 on 2021-12-11 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('two_sum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numbers',
            name='costing',
        ),
    ]