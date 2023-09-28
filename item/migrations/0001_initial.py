# Generated by Django 4.2.5 on 2023-09-28 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=45)),
                ('item_qty', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=7, null=True)),
                ('item_unit', models.CharField(blank=True, max_length=8, null=True)),
                ('wholesale_rate', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=7, null=True)),
                ('retail_rate', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=7, null=True)),
                ('outside_rate', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=7, null=True)),
                ('product_charge', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=7, null=True)),
                ('vehicle_rent_wholesale_rate', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=7, null=True)),
                ('vehicle_rent_retail_rate', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=7, null=True)),
                ('vehicle_rent_outside_rate', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=7, null=True)),
                ('vehicle_rent_factory_outside_rate', models.DecimalField(
                    blank=True, decimal_places=2, max_digits=7, null=True)),
                ('wrapping', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=7, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(db_column='created_by', null=True,
                 on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_at', models.DateTimeField(null=True)),
                ('updated_by', models.ForeignKey(db_column='updated_by', null=True,
                 on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
