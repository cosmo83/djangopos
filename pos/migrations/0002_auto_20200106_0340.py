# Generated by Django 2.0.13 on 2020-01-06 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_squashed_0037_remove_store_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Storage Location', 'verbose_name_plural': 'Storage Locations'},
        ),
        migrations.AlterField(
            model_name='sale',
            name='store',
            field=models.ForeignKey(limit_choices_to={'is_deleted': False, 'is_sale_location': True}, on_delete=django.db.models.deletion.CASCADE, to='pos.Store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='addr1',
            field=models.CharField(max_length=200, verbose_name='Address 1'),
        ),
    ]