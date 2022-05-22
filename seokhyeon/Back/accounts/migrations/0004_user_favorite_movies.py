# Generated by Django 3.2 on 2022-05-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movie_favorite_users'),
        ('accounts', '0003_delete_favoritemovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_movies',
            field=models.ManyToManyField(related_name='favorite_users', to='movies.Movie'),
        ),
    ]