# Generated by Django 2.0.13 on 2020-01-05 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0021_auto_20200105_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hsncode',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pos.TaxesGST'),
            preserve_default=False,
        ),
    ]