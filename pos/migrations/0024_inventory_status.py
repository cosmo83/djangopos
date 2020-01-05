# Generated by Django 2.0.13 on 2020-01-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0023_auto_20200105_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='status',
            field=models.IntegerField(choices=[(0, 'In Store'), (1, 'Sold'), (2, 'In Transit')], default=0, verbose_name='Status'),
            preserve_default=False,
        ),
    ]
