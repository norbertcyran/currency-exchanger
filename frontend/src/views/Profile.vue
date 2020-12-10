<template>
  <v-container>
    <v-layout align-center justify-center>
      <v-flex xs8 sm8 md6>
        <v-form>
          <v-card class="elevation-12">
            <v-toolbar dark color="blue">
              <v-toolbar-title> Profile </v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              Recent Transactions
              <TransferCard
                v-for="(el, index) in userTransfers"
                :key="index"
                :currency="el.currency"
                :amount="el.amount"
                :isOutgoing="el.isOutgoing"
                :otherUser="el.otherUser"
                :title="el.title"
              ></TransferCard>
              <CurrencyExchangeCard
                v-for="(el, index) in userCurrencyExchanges"
                :key="index"
                :currencyFrom="el.currencyFrom"
                :currencyTo="el.currencyTo"
                :fromAmount="el.fromAmount"
                :toAmount="el.toAmount"
                :rate="el.rate"
              ></CurrencyExchangeCard>
              <StockCard
                v-for="(el, index) in userStockTransactions"
                :key="index"
                :currency="el.currency"
                :currencyAmount="el.currencyAmount"
                :stockName="el.stockName"
                :stockAmount="el.stockAmount"
                :time="el.time"
              ></StockCard>
            </v-card-text>
            <v-divider light></v-divider>
          </v-card>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import TransferCard from "../components/ProfileTransactions/TransferCard";
import CurrencyExchangeCard from "../components/ProfileTransactions/CurrencyExchangeCard";
import StockCard from "../components/ProfileTransactions/StockCard";
export default {
  data: () => ({
    recentTransactions: [],
    userTransfers: [
      {
        title: "money transfer1",
        isOutgoing: true,
        amount: 41,
        otherUser: "gaws@gmail.com",
        currency: "zloty",
      },
      {
        title: "money transfer2",
        isOutgoing: false,
        amount: 41,
        otherUser: "gaws@gmail.com",
        currency: "zloty",
      },
    ],
    userCurrencyExchanges: [
      {
        currencyFrom: "zloty",
        currencyTo: "euro",
        fromAmount: 12,
        toAmount: 48,
        rate: 4,
      },
    ],

    userStockTransactions: [
      {
        currency: "zloty",
        currencyAmount: 45,
        stockName: "Tesla",
        stockAmount: 2,
      },
    ],
  }),
  components: {
    TransferCard,
    CurrencyExchangeCard,
    StockCard,
  },
};
</script>
