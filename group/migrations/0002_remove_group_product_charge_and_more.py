# Generated by Django 4.2.5 on 2023-09-27 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='product_charge',
        ),
        migrations.RemoveField(
            model_name='group',
            name='vehicle_rent',
        ),
        migrations.RemoveField(
            model_name='group',
            name='wrapping',
        ),
    ]
