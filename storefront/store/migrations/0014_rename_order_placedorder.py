# Generated by Django 3.2.9 on 2021-12-03 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_order_orderitem_order_field'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='PlacedOrder',
        ),
    ]
