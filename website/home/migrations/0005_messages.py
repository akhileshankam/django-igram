# Generated by Django 3.1.4 on 2021-02-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210216_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromusername', models.CharField(default=1, max_length=50)),
                ('mssg', models.CharField(default=1, max_length=5000)),
                ('tousername', models.CharField(default=1, max_length=50)),
            ],
        ),
    ]
