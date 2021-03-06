# Generated by Django 2.2.7 on 2019-12-24 14:36

from django.db import migrations, models
import pos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[pos.models.validate_product_name])),
                ('item_code', models.CharField(max_length=50, unique=True, verbose_name='Item Code')),
                ('code', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='UPC Code')),
                ('hsncode', models.CharField(max_length=20, verbose_name='HSN Code')),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
