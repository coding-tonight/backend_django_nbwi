# Generated by Django 4.2.5 on 2023-09-27 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factoryowner',
            name='factory_id',
            field=models.OneToOneField(db_column='factory_id', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='factory.factory'),
        ),
    ]