# Generated by Django 4.2.5 on 2023-09-27 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0002_remove_group_product_charge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='updated_by',
            field=models.ForeignKey(db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
