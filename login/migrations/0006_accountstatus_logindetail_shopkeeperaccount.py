# Generated by Django 3.0.3 on 2020-03-10 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0005_auto_20200310_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('status_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'account_status',
            },
        ),
        migrations.CreateModel(
            name='ShopKeeperAccount',
            fields=[
                ('account_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100, unique=True)),
                ('phone_no', models.PositiveIntegerField()),
                ('created_by', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.AccountStatus')),
            ],
            options={
                'db_table': 'shop_keeper_account',
            },
        ),
        migrations.CreateModel(
            name='LoginDetail',
            fields=[
                ('login_detail_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('salt', models.CharField(max_length=10)),
                ('account_type', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ShopKeeperAccount')),
            ],
            options={
                'db_table': 'login_detail',
            },
        ),
    ]
