<template>
  <v-card width="400px" class="mt-4" display="block">
    <v-toolbar-title>
      <!-- <h4>rate: {{this.exchangeRate}}</h4> -->
    </v-toolbar-title>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="6">
          <v-combobox
            v-model="fromCurrency"
            label="From"
            @change="getExchangeRate"
            :items="userCurrencies"
            outlined
            dense
          ></v-combobox>
        </v-col>

        <v-col cols="12" sm="6" md="6">
          <v-text-field
            v-model="fromCurrencyAmount"
            label="Solo"
            placeholder="Amount"
            solo
            :rules="[rules.required]"
            @change="updateNewCurrencyAmount"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-combobox
            v-model="toCurrency"
            label="To"
            :items="allCurrencies"
            outlined
            dense
            @change="updateNewCurrencyAmount"
          ></v-combobox>
        </v-col>

        <v-col cols="12" sm="6" md="6">
          <v-text-field
            label=""
            solo
            disabled
            v-model="toCurrencyAmount"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-container>
    <v-card-actions>
      <v-layout align-center justify-center
        ><v-btn color="indigo" dark a @click="exchangeCurrency">Change currency</v-btn>
      </v-layout>
    </v-card-actions>
  </v-card>
</template>
<script>
import currenciesAPI from "../api/currencies";
import { mapGetters} from "vuex";



export default {
  data: () => ({
    currenciesAndAmount: [
      {
        currency: "zloty",
        amount: 24
      },
      {
        currency: "dollar",
        amount: 30
      }
    ],
    allCurrencies: ["dollar", "zloty", "euro", "yen"],
    exchangeRate: 3.65,
    fromCurrency: "",
    toCurrency: "",
    fromCurrencyAmount: 0,
    toCurrencyAmount: 0,

    rules: {
      //   limitAmount:  value => value <= this.maxAmount || "you cannot exceed your limit",
      required: value => !!value || "Required."
    }
  }),



  computed: {



    userCurrencies: function() {
      var res = this.currenciesAndAmount.map(cur => cur.currency);
      return res;
    },
    maxAmount: function() {
      for (var i = 0; i < this.currenciesAndAmount.length; i++) {
        if (this.currenciesAndAmount[i].currency === this.fromCurrency) {
          return this.currenciesAndAmount[i].amount;
        }
      }
      return 0;
    },
    ...mapGetters(["wallet"]),

    formData() {
      return {
        currency_from: this.fromCurrency,
        currency_to: this.toCurrency,
        amount: this.fromCurrencyAmount,
      };
    }

  },


  methods: {

    async getAllCurrencies(){
        const response = await currenciesAPI.getCurrencies();
        this.allCurrencies = response.data.map(c=>c.code);
        return response.data;
    },

    async updateNewCurrencyAmount() {
      this.getExchangeRate();
      this.toCurrencyAmount = parseFloat(this.fromCurrencyAmount) * this.exchangeRate;
    },
    async getUserCurrrencies() {
      try {
        this.currenciesAndAmount = this.wallet.currencies;
      } catch (err) {
        console.log(err);
      }
    },
    async getExchangeRate() {
      if (this.fromCurrency && this.toCurrency)
        try {
          const from = await currenciesAPI.getExchangeRate(this.fromCurrency);
          const to = await currenciesAPI.getExchangeRate(this.toCurrency);
          this.exchangeRate = Math.round(parseFloat(to.data[0].rate) / parseFloat(from.data[0].rate)*100)/100;
        } catch (err) {
          console.log(err);
        }
    },
    async exchangeCurrency(){
        try {
            currenciesAPI.makeExchange(this.formData);
        } catch (error) {
            console.log(error);
        }
    },
  },
   created(){
      this.getUserCurrrencies();
      this.getAllCurrencies();
  },
};
</script>
