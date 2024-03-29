# Generated by Django 3.1.2 on 2020-12-07 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
        ('stocks', '0003_add_unique_constraints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletstock',
            name='stocks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.stock'),
        ),
        migrations.AlterField(
            model_name='walletstock',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallets.wallet'),
        ),
    ]
