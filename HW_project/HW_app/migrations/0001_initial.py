# Generated by Django 5.0.2 on 2024-03-25 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('registration_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_of_products', models.IntegerField()),
                ('add_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/upload')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_ordered', models.DateTimeField()),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HW_app.client')),
                ('products', models.ManyToManyField(to='HW_app.product')),
            ],
        ),
    ]
