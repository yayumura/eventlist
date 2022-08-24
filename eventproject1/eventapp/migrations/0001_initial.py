# Generated by Django 4.1 on 2022-08-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='開催日')),
                ('title', models.CharField(max_length=128, verbose_name='イベント名')),
                ('link', models.CharField(max_length=128, verbose_name='リンク')),
            ],
        ),
    ]