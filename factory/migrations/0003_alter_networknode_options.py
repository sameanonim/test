# Generated by Django 4.2.6 on 2023-10-08 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0002_networknode_remove_supplier_products_factory_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='networknode',
            options={'ordering': ['level', 'name']},
        ),
    ]
