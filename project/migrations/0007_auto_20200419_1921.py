# Generated by Django 3.0.5 on 2020-04-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20200419_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
