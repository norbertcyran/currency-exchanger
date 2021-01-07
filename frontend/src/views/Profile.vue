Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@macikoj 
norbertcyran
/
currency-exchanger
Private
2
00
Code
Issues
4
Pull requests
1
Actions
Projects
1
Wiki
Security
Insights
currency-exchanger/frontend/src/views/Profile.vue
@macikoj
macikoj some fixes
Latest commit 6550ec7 2 days ago
 History
 2 contributors
@macikoj@norbertcyran
109 lines (109 sloc)  3.07 KB
  
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
                :currencyFrom="el.currency_from"
                :currencyTo="el.currency_to"
                :fromAmount="parseFloat(el.amount)"
                :toAmount="parseFloat(el.amount_to)"
              ></CurrencyExchangeCard>
              <StockCard
                v-for="(el, index) in userStockTransactions"
                :key="index"
                :currencyAmount="parseFloat(el.price)"
                :stockName="el.stock"
                :stockAmount="parseInt(el.amount)"
                :time="el.id"
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
import currenciesAPI from "../api/currencies"
import stocksAPI from "../api/stocks"
import transferAPI from '../api/transfers'
export default {
  data: () => ({
    recentTransactions: [],
    userTransfers: [],
    userCurrencyExchanges: [],
    userStockTransactions: [],
  }),
  components: {
    TransferCard,
    CurrencyExchangeCard,
    StockCard,
  },
  methods:{
    async getUserExchanges() {
      try {
       const response =await currenciesAPI.getCurrencyExchanges()
        this.userCurrencyExchanges = response.data;
      } catch (err) {
        console.log(err);
      }
    },
    async getUserStockTransfers() {
      try {
       const response =await stocksAPI.getStockTransfers()
        this.userStockTransactions = response.data;
      } catch (err) {
        console.log(err);
      }
    },
        async getUserTransfers() {
      try {
       const response =await transferAPI.getTransfers()
        this.userTransfers = response.data;
      } catch (err) {
        console.log(err);
      }
    },
  },
 mounted(){
   this.getUserExchanges()
   this.getUserStockTransfers()
   this.getUserTransfers()
  }
};
</script>