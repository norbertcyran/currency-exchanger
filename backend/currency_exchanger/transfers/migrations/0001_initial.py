# Generated by Django 3.1.2 on 2020-11-08 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallets', '0001_initial'),
        ('currencies', '0002_auto_20201108_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='currencies.currency')),
                ('wallet_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_transfers', to='wallets.wallet')),
                ('wallet_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_transfers', to='wallets.wallet')),
            ],
        ),
    ]