# Generated by Django 4.0 on 2021-12-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=100)),
                ('target', models.IntegerField()),
                ('costing', models.CharField(max_length=155)),
            ],
        ),
    ]
