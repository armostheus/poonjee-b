# Generated by Django 2.2 on 2019-04-18 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poonjeeMain', '0002_auto_20190417_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_details',
            name='transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poonjeeMain.Sales_Transactions'),
        ),
    ]