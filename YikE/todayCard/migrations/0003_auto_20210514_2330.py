# Generated by Django 3.1.7 on 2021-05-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todayCard', '0002_auto_20210513_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todaycard',
            name='state',
            field=models.IntegerField(choices=[(0, 'Ing Check'), (1, 'Ed Check')]),
        ),
    ]