# Generated by Django 3.2.7 on 2021-11-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offer',
            new_name='Voucher',
        ),
    ]
