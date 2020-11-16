from django.db.models.signals import post_save
from django.dispatch import receiver
from currency_exchanger.users.models import User
from currency_exchanger.wallets.serializers import WalletSerializer



@receiver(post_save, sender=User)
def create_wallet(sender,instance,created, **kwargs):
    if created:
        data = {"user": instance}
        WalletSerializer().create(validated_data=data)
