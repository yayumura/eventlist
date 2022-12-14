# Generated by Django 4.1 on 2022-08-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='開催日')),
                ('title', models.CharField(max_length=128, verbose_name='イベント名')),
                ('link', models.URLField(verbose_name='リンク')),
                ('category', models.CharField(choices=[('game', 'ゲーム'), ('anime', 'アニメ'), ('eat', '食事'), ('other', 'その他')], max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='EventModel',
        ),
    ]
