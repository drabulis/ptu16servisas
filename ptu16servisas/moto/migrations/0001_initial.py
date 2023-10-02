# Generated by Django 4.2.5 on 2023-10-02 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50, verbose_name='Make')),
                ('model', models.CharField(max_length=50, verbose_name='Model')),
                ('year', models.IntegerField()),
            ],
            options={
                'verbose_name': 'CarModel',
                'verbose_name_plural': 'CarModels',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('plate', models.CharField(db_index=True, max_length=10, verbose_name='Plate')),
                ('vin', models.CharField(max_length=17, verbose_name='VIN')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('car_model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='moto.carmodel', verbose_name='Car')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
            },
        ),
        migrations.CreateModel(
            name='PartService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'PartService',
                'verbose_name_plural': 'PartServices',
            },
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_orders', to='moto.customer', verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'ServiceOrder',
                'verbose_name_plural': 'ServiceOrders',
                'ordering': ['customer_id'],
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantinity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Reserved'), (1, 'Working'), (2, 'Done'), (3, 'Canceled')], db_index=True, default=0, verbose_name='Status')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='moto.serviceorder', verbose_name='Customer')),
                ('part_service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='moto.partservice', verbose_name='Service')),
            ],
            options={
                'verbose_name': 'OrderLine',
                'verbose_name_plural': 'OrderLines',
                'ordering': ['order_id', 'part_service_id', 'status'],
            },
        ),
    ]
