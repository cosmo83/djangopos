# Generated by Django 2.2.7 on 2019-12-25 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='store',
            field=models.ForeignKey(default=1, limit_choices_to={'is_deleted': False, 'is_sale_location': True}, on_delete=django.db.models.deletion.CASCADE, to='pos.Store'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sale',
            name='status',
            field=models.IntegerField(choices=[(0, 'Sale Completed'), (1, 'Sale in Progress'), (2, 'Sale Cancelled')], default=False, verbose_name='Sale Status'),
        ),
    ]
