# Generated by Django 2.0.13 on 2019-12-31 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_saleline_is_product_serial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=7)),
                ('serialbatchnumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='Serial / Batch Number')),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('sale', 'Sale'), ('cost', 'Cost')], max_length=10, verbose_name='Price List Type')),
                ('serialbatchnumber', models.CharField(max_length=50, verbose_name='Serial/Batch Number')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='is_product_serial',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='UPC Code'),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Product'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Product'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Store'),
        ),
    ]
