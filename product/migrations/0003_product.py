# Generated by Django 4.2.9 on 2024-06-10 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Purchase_Date', models.DateField()),
                ('Invoice_Number', models.IntegerField()),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.item')),
                ('Supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.supplier')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
