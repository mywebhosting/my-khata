# Generated by Django 3.0.3 on 2020-03-10 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_accountstatus_logindetail_shopkeeperaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logindetail',
            name='account_id',
        ),
        migrations.RemoveField(
            model_name='shopkeeperaccount',
            name='status_id',
        ),
        migrations.DeleteModel(
            name='AccountStatus',
        ),
        migrations.DeleteModel(
            name='LoginDetail',
        ),
        migrations.DeleteModel(
            name='ShopKeeperAccount',
        ),
    ]
