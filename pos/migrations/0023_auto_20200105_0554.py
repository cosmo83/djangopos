# Generated by Django 2.0.13 on 2020-01-05 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0022_product_hsncode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxesgst',
            old_name='name',
            new_name='hsnname',
        ),
    ]
