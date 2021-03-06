# Generated by Django 3.2.8 on 2021-11-24 15:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MovieReview', '0003_alter_movie_review_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_review',
            name='likes',
            field=models.ManyToManyField(related_name='review', to=settings.AUTH_USER_MODEL),
        ),
    ]
