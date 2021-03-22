# Generated by Django 3.1.7 on 2021-03-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('date_published', models.DateTimeField(auto_now=True, verbose_name='Data de publicação')),
                ('slug', models.SlugField(editable=False, verbose_name='Slug')),
            ],
        ),
    ]
