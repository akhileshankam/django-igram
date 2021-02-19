# Generated by Django 3.1.4 on 2021-02-16 09:44

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
                ('title', models.CharField(default=2, max_length=50)),
                ('username', models.CharField(default=1, max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('likes', models.CharField(default=1, max_length=50)),
            ],
        ),
    ]