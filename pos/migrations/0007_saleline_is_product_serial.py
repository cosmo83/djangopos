# Generated by Django 2.0.13 on 2019-12-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_saleline'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleline',
            name='is_product_serial',
            field=models.BooleanField(default=False),
        ),
    ]
