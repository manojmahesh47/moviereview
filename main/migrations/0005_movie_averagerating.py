# Generated by Django 4.2.7 on 2024-01-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='averageRating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
