# Generated by Django 4.1.7 on 2023-04-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_actor_comment_director_slug_movie_avg_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='photo_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]