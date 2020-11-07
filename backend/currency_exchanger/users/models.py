from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="info")
    phone = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=200)

    def __str__(self):
        return self.user


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet")
    money = models.DecimalField(max_length=20)


class Currency(models.Model):
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=255)
    rate = models.DecimalField(max_length=20)



class WalletCurrency(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE, related_name= "wallet")
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE, related_name= "currency")
    value = models.DecimalField(max_length=20)


class CurrencyHistory(models.Model):
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE, related_name= "currency")
    timestamp = models.DateTimeField()
    rate = models.DecimalField(max_length=20)


class CurrencyExchange(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="wallet")
    currency_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="from")
    currency_to = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name= "to")


class MoneyTransfer(models.Model):
    wallet_from = models.ForeignKey(Wallet,on_delete=models.CASCADE, related_name="from")
    wallet_to = models.ForeignKey(Wallet,on_delete=models.CASCADE, related_name="to")
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE, related_name="currency")
    value = models.DecimalField(max_length=10)


class Stocks(models.Model):
    code = models.CharField(max_length=10)
    price = models.DecimalField(max_length=20)


class WalletStocks(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE, related_name="wallet")
    stocks = models.ForeignKey(Stocks, on_delete= models.CASCADE, related_name="stocks")
    count = models.IntegerField(max_length=20)


class StocksShareBuys:
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE, related_name= "wallet")
    stocks = models.ForeignKey(Stocks, on_delete= models.CASCADE, related_name="stocks")
    count = models.IntegerField(max_length=20)


class StockHistory:
    stocks = models.ForeignKey(Stocks, on_delete= models.CASCADE, related_name="stocks")
    timestamp = models.DateTimeField()
    price = models.DecimalField(max_length=20)




