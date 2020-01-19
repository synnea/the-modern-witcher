# Generated by Django 2.2 on 2020-01-19 17:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0002_item_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Test', max_length=50)),
                ('phone_number', models.CharField(default=0, max_length=20)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.Item')),
            ],
        ),
    ]
