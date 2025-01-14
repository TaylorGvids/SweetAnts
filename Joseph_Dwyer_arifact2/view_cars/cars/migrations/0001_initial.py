# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-22 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CentralDatabase',
            fields=[
                ('order_id', models.IntegerField(db_column='order_ID', primary_key=True, serialize=False)),
                ('order_createdate', models.DateField(blank=True, db_column='Order_CreateDate', null=True)),
                ('order_pickupdate', models.DateField(blank=True, db_column='Order_PickupDate', null=True)),
                ('order_pickupstore', models.IntegerField(blank=True, db_column='Order_PickupStore', null=True)),
                ('pickup_store_name', models.CharField(blank=True, db_column='Pickup_Store_Name', max_length=21, null=True)),
                ('pickup_store_address', models.CharField(blank=True, db_column='Pickup_Store_Address', max_length=25, null=True)),
                ('pickup_store_phone', models.CharField(blank=True, db_column='Pickup_Store_Phone', max_length=19, null=True)),
                ('pickup_store_city', models.CharField(blank=True, db_column='Pickup_Store_City', max_length=30, null=True)),
                ('pickup_store_state_name', models.CharField(blank=True, db_column='Pickup_Store_State_Name', max_length=15, null=True)),
                ('order_returndate', models.IntegerField(blank=True, db_column='Order_ReturnDate', null=True)),
                ('order_returnstore', models.IntegerField(blank=True, db_column='Order_ReturnStore', null=True)),
                ('return_store_name', models.CharField(blank=True, db_column='Return_Store_Name', max_length=21, null=True)),
                ('return_store_address', models.CharField(blank=True, db_column='Return_Store_Address', max_length=25, null=True)),
                ('return_store_phone', models.CharField(blank=True, db_column='Return_Store_Phone', max_length=19, null=True)),
                ('return_store_city', models.CharField(blank=True, db_column='Return_Store_City', max_length=30, null=True)),
                ('return_store_state', models.CharField(blank=True, db_column='Return_Store_State', max_length=15, null=True)),
                ('customer_id', models.IntegerField(blank=True, db_column='Customer_ID', null=True)),
                ('customer_name', models.CharField(blank=True, db_column='Customer_Name', max_length=12, null=True)),
                ('customer_phone', models.CharField(blank=True, db_column='Customer_Phone', max_length=19, null=True)),
                ('customer_addresss', models.CharField(blank=True, db_column='Customer_Addresss', max_length=30, null=True)),
                ('customer_brithday', models.CharField(blank=True, db_column='Customer_Brithday', max_length=10, null=True)),
                ('customer_occupation', models.CharField(blank=True, db_column='Customer_Occupation', max_length=10, null=True)),
                ('customer_gender', models.CharField(blank=True, db_column='Customer_Gender', max_length=3, null=True)),
                ('car_id', models.IntegerField(db_column='Car_ID')),
                ('car_makename', models.CharField(blank=True, db_column='Car_MakeName', max_length=13, null=True)),
                ('car_model', models.CharField(blank=True, db_column='Car_Model', max_length=15, null=True)),
                ('car_series', models.CharField(blank=True, db_column='Car_Series', max_length=35, null=True)),
                ('car_seriesyear', models.CharField(blank=True, db_column='Car_SeriesYear', max_length=4, null=True)),
                ('car_pricenew', models.CharField(blank=True, db_column='Car_PriceNew', max_length=6, null=True)),
                ('car_enginesize', models.CharField(blank=True, db_column='Car_EngineSize', max_length=4, null=True)),
                ('car_fuelsystem', models.CharField(blank=True, db_column='Car_FuelSystem', max_length=18, null=True)),
                ('car_tankcapacity', models.CharField(blank=True, db_column='Car_TankCapacity', max_length=5, null=True)),
                ('car_power', models.CharField(blank=True, db_column='Car_Power', max_length=5, null=True)),
                ('car_seatingcapacity', models.CharField(blank=True, db_column='Car_SeatingCapacity', max_length=2, null=True)),
                ('car_standardtransmission', models.CharField(blank=True, db_column='Car_StandardTransmission', max_length=5, null=True)),
                ('car_bodytype', models.CharField(blank=True, db_column='Car_BodyType', max_length=14, null=True)),
                ('car_drive', models.CharField(blank=True, db_column='Car_Drive', max_length=3, null=True)),
                ('car_wheelbase', models.CharField(blank=True, db_column='Car_Wheelbase', max_length=6, null=True)),
            ],
            options={
                'db_table': 'central database',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instore',
            fields=[
                ('store_id', models.IntegerField(db_column='store_ID')),
                ('store_name', models.CharField(blank=True, db_column='Store_Name', max_length=50, null=True)),
                ('store_address', models.CharField(blank=True, db_column='Store_Address', max_length=50, null=True)),
                ('store_phone', models.CharField(blank=True, db_column='Store_Phone', max_length=19, null=True)),
                ('store_city', models.CharField(blank=True, db_column='Store_City', max_length=50, null=True)),
                ('store_state_name', models.CharField(blank=True, db_column='Store_State_Name', max_length=50, null=True)),
                ('order_id', models.IntegerField(blank=True, db_column='Order_ID', null=True)),
                ('order_createdate', models.DateField(blank=True, db_column='Order_CreateDate', null=True)),
                ('pickup_or_return', models.CharField(blank=True, db_column='Pickup_Or_Return', max_length=50, null=True)),
                ('pickup_or_return_date', models.DateField(blank=True, db_column='Pickup_Or_Return_Date', null=True)),
                ('customer_id', models.IntegerField(db_column='Customer_ID', primary_key=True, serialize=False)),
                ('customer_name', models.CharField(blank=True, db_column='Customer_Name', max_length=50, null=True)),
                ('customer_phone', models.CharField(blank=True, db_column='Customer_Phone', max_length=50, null=True)),
                ('customer_addresss', models.CharField(blank=True, db_column='Customer_Addresss', max_length=50, null=True)),
                ('customer_birthday', models.CharField(blank=True, db_column='Customer_Birthday', max_length=8, null=True)),
                ('customer_occupation', models.CharField(blank=True, db_column='Customer_Occupation', max_length=50, null=True)),
                ('customer_gender', models.CharField(blank=True, db_column='Customer_Gender', max_length=50, null=True)),
                ('car_id', models.IntegerField(blank=True, db_column='Car_ID', null=True)),
                ('car_makename', models.CharField(blank=True, db_column='Car_MakeName', max_length=50, null=True)),
                ('car_model', models.CharField(blank=True, db_column='Car_Model', max_length=50, null=True)),
                ('car_series', models.CharField(blank=True, db_column='Car_Series', max_length=50, null=True)),
                ('car_seriesyear', models.CharField(blank=True, db_column='Car_SeriesYear', max_length=4, null=True)),
                ('car_pricenew', models.CharField(blank=True, db_column='Car_PriceNew', max_length=6, null=True)),
                ('car_enginesize', models.CharField(blank=True, db_column='Car_EngineSize', max_length=4, null=True)),
                ('car_fuelsystem', models.CharField(blank=True, db_column='Car_FuelSystem', max_length=50, null=True)),
                ('car_tankcapacity', models.CharField(blank=True, db_column='Car_TankCapacity', max_length=5, null=True)),
                ('car_power', models.CharField(blank=True, db_column='Car_Power', max_length=50, null=True)),
                ('car_seatingcapacity', models.CharField(blank=True, db_column='Car_SeatingCapacity', max_length=2, null=True)),
                ('car_standardtransmission', models.CharField(blank=True, db_column='Car_StandardTransmission', max_length=50, null=True)),
                ('car_bodytype', models.CharField(blank=True, db_column='Car_BodyType', max_length=50, null=True)),
                ('car_drive', models.CharField(blank=True, db_column='Car_Drive', max_length=3, null=True)),
                ('car_wheelbase', models.CharField(blank=True, db_column='Car_Wheelbase', max_length=6, null=True)),
            ],
            options={
                'db_table': 'instore',
                'managed': False,
            },
        ),
    ]
