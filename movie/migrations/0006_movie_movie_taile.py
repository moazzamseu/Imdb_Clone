# Generated by Django 3.0.7 on 2020-06-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_taile',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
