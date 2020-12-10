# Generated by Django 3.1.2 on 2020-12-06 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currencies', '0003_add_unique_constraints'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='currencies.currency')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_transfers', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_transfers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
