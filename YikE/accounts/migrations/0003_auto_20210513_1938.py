# Generated by Django 3.1.7 on 2021-05-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todayCard', '0002_auto_20210513_1857'),
        ('accounts', '0002_auto_20210513_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='collectid',
        ),
        migrations.AddField(
            model_name='user',
            name='collectid',
            field=models.ManyToManyField(blank=True, related_name='collectid', to='todayCard.TodayCard'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='contributeid',
        ),
        migrations.AddField(
            model_name='user',
            name='contributeid',
            field=models.ManyToManyField(blank=True, related_name='contributeid', to='todayCard.TodayCard'),
        ),
    ]
