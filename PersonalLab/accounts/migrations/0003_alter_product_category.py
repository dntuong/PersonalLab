# Generated by Django 4.0.4 on 2022-04-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor1'), ('Outdoor', 'Outdoor1')], max_length=200, null=True),
        ),
    ]
