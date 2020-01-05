# Generated by Django 2.0.13 on 2020-01-02 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0010_remove_product_sell_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxesGST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsncode', models.CharField(max_length=20, verbose_name='HSN Code')),
                ('taxrate', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Inventory', 'verbose_name_plural': 'Inventory Lines'},
        ),
        migrations.AlterField(
            model_name='product',
            name='hsncode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.TaxesGST'),
        ),
    ]