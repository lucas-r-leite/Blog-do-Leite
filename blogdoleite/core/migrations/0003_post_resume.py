# Generated by Django 3.1.7 on 2021-03-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210322_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resume',
            field=models.TextField(default=''),
        ),
    ]
