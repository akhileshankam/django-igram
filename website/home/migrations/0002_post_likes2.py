# Generated by Django 3.1.4 on 2021-02-16 09:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes2',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
